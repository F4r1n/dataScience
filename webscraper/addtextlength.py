import os
import json

with open("list.txt", 'r') as list:
    with open("features.json", "r+") as jsonFile:
        #load json object
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
                #corrected lines which will be used to overwrite the file
                newLines = ""
                #open file to strip whitespaces and remove empty lines
                with open("./data/" + movieString + ".txt", "r") as file:
                    for line in file:
                        newLine = line.strip()
                        if len(newLine) == 0:
                            continue
                        else:
                            newLines += newLine + "\n"
                #reopen the file in write mode to overwrite it with newLines
                with open("./data/" + movieString + ".txt", "w") as file:
                    file.write(newLines)
                #add length field to corresponding movie in json
                data[movie]["length"] = len(newLines.split(" "))
            except:
                print("File for movie %s not found" % movieString)
        #write json
        jsonFile.seek(0)
        json.dump(data, jsonFile, indent=4)
        jsonFile.truncate()
