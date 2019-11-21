import requests
import bs4
import re
import json

def featureToFile(movieString, response):
    soup = bs4.BeautifulSoup(response, features="lxml")
    #Year in which the movie was published
    yearPublished = soup.find_all("b", string="Movie Release Date")
    if yearPublished:
        year = yearPublished[0].next_element.next_element
        year = year.replace(":", "")
        year = year.strip()
        return (year)
    else:
        return None

with open("list.txt", 'r') as list:
    with open("features.json", "r+") as jsonFile:
        #load json object
        data = json.load(jsonFile)
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
                year = featureToFile(movie, res.text)
                if year != None:
                    data[movie]["released"] = year

        jsonFile.seek(0)
        json.dump(data, jsonFile, indent=4)
        jsonFile.truncate()
