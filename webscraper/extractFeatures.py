import requests
import bs4
import re
import pandas as pd

masterDict = {}

def featureToFile(movieString, response):
    soup = bs4.BeautifulSoup(response, features="lxml")
    genres = soup.find_all('a', {'href': re.compile(r'/genre/')})
    writers = soup.find_all('a', {'href': re.compile(r'/writer.php')})

    genresForDict = []
    writersForDict = []
    for index, genre in enumerate(genres):
        if (index > 17):
            genresForDict.append(genre.getText())
    for writer in writers:
        writersForDict.append(writer.getText())
    masterDict[movieString] = {"genres": genresForDict, "writers": writersForDict}

with open("list.txt", 'r') as list:
        #iterate file line by line
        for movie in list:
            #replace newlines for formatting
            movie = movie.replace("\n", "")
            movieStringForURL = movie.replace(" ", "%20")

            #request the page with the script
            res = requests.get('https://www.imsdb.com/Movie%20Scripts/' +
                            movieStringForURL + '%20Script.html')
            #if okay call function that saves the script
            print(movie)
            if res.ok:
                featureToFile(movie, res.text)

df = pd.DataFrame(masterDict)
df.to_json("features.json")