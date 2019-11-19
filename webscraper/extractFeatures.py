import requests
import bs4
import re
import pandas as pd

masterDict = {}

def featureToFile(movieString, response):
    soup = bs4.BeautifulSoup(response, features="lxml")
    #links of genres on page of moviescript
    genres = soup.find_all('a', {'href': re.compile(r'/genre/')})
    #links of writers on page of moviescript
    writers = soup.find_all('a', {'href': re.compile(r'/writer.php')})

    genresForDict = []
    writersForDict = []
    for index, genre in enumerate(genres):
        #first 17 are a list of all genres so we will skip those
        if (index > 17):
            #write movie genres in array
            genresForDict.append(genre.getText())
    for writer in writers:
        #write writers in array
        writersForDict.append(writer.getText())
    #make new index in dict and assign both arrays
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

#put dict in dataframe
df = pd.DataFrame(masterDict)
#write dataframe as json file
df.to_json("features.json")
