import os
import json

with open("list.txt", 'r') as list:
    with open("features.json", "r+") as jsonFile:
        #load json object
        data = json.load(jsonFile)
        genres = []
        genreCount = {}
        totalLength = 0
        lengthCount = 0
        # iterate file line by line
        for movie in list:
            movie = movie.replace("\n", "")
            # replace blank spaces with - to use in the url
            movieString = movie.replace(" ", "-")
            # replace : because its not used by the site in the url
            movieString = movieString.replace(":", "")
            try:
                for genre in data[movie]["genres"]:
                    genres.append(genre)
                lengthCount = lengthCount + 1
                totalLength = totalLength + data[movie]["length"]
            except:
                print("File for movie %s not found" % movieString)
        genreSet = set(genres)
        for genre in genreSet:
            count = genres.count(genre)
            genreCount[genre] = count
        print({k: v for k, v in sorted(genreCount.items(), key=lambda item: item[1])})
        print(totalLength/lengthCount)
