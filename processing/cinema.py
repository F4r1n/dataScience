import requests
import json
import os

#using the omdbapi, turned out that the year taken from the script page (IMSDB.com) was not always correct and we eneded up with bad data. Data was corrected manually  

def getMovieInfo(name, year, api):
    url = "http://www.omdbapi.com/?t=%s&y=%s&apikey=%s" % (name.replace(" ", "+"), year, api)
    response = requests.request("GET", url)
    obj = json.loads(response.text.encode('utf8'))

    #on error retry without years
    if (obj["Response"] == "False"):
        url = "http://www.omdbapi.com/?t=%s&apikey=%s" % (name.replace(" ", "+"), api)
        response = requests.request("GET", url)
        obj = json.loads(response.text.encode('utf8'))

    return(obj)

apiKey = "10a8260"
with open("features.json", "r+") as jsonFile:
    data = json.load(jsonFile)
    with open("list.txt", 'r') as list:
        for movie in list:
            movie = movie.replace("\n", "")
            # replace blank spaces with - to use in the url
            movieString = movie.replace(" ", "-")
            # replace : because its not used by the site in the url
            movieString = movieString.replace(":", "")
            if (',' in movie):
                tempMovie = movie.split(',')
                movieForFunc = tempMovie[1] + " " + tempMovie[0]
            else:
                movieForFunc = movie

            try:
                year = data[movie]["released"][-4:]
            except:
                year = ""
            
            obj = getMovieInfo(movieForFunc, year, apiKey)
            if (obj["Response"] == "False"):
                print(obj)
                print(movie)
            else:
                #;)
                # if ("Error" in obj):
                #     if (obj["Error"] == "Request limit reached!"):
                #         #Use second api key when 1000 requests are used
                #         obj = getMovieInfo(movieForFunc, year, apiKey)
                try:
                    data[movie]["Year"] = obj["Year"]
                    data[movie]["Runtime"] = obj["Runtime"]
                    data[movie]["imdbRating"] = obj["imdbRating"]
                    data[movie]["imdbID"] = obj["imdbID"]
                    data[movie]["BoxOffice"] = obj["BoxOffice"]
                except KeyError:
                    print("ERROR: " + movie)
    jsonFile.seek(0)
    json.dump(data, jsonFile, indent=4)
    jsonFile.truncate()