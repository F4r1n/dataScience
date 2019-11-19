import os
import json

with open("list.txt", 'r') as list:
    with open("features.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        # iterate file line by line
        for movie in list:
            movie = movie.replace("\n", "")
            # replace blank spaces with - to use in the url
            movieString = movie.replace(" ", "-")
            # replace : because its not used by the site in the url
            movieString = movieString.replace(":", "")
            print(movieString)
            try:
                newLines = ""
                with open("./data/" + movieString + ".txt", "r") as file:
                    for line in file:
                        newLine = line.strip()
                        if len(newLine) == 0:
                            continue
                        else:
                            newLines += newLine + "\n"
                with open("./data/" + movieString + ".txt", "w") as file:
                    file.write(newLines)
                data[movie]["length"] = len(newLines)
            except:
                print("File for movie %s not found" % movieString)
        jsonFile.seek(0)
        json.dump(data, jsonFile, indent=4)
        jsonFile.truncate()
