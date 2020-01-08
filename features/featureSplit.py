import json

# TURNS OUT THIS IS NOT THE WAY TO GO. Generates invalid json
# This function requires some manual formatting because i was lazy. Remove last comma in file and add { to the beginning and } to the end


def reformatJson():
    with open("./features/features.json", "r+") as features:
        data = json.load(features)
        with open("./features/newFeatures.json", "w") as new:
            for movie in data:
                print(movie)
                data[movie]["title"] = movie
                obj = json.dumps(data[movie])
                new.write(obj + ",\n")

# I wanted to check if and which elements are missing by counting and printing all the fields


def checkAttributeCount():
    with open("./features/features.json", "r+") as features:
        data = json.load(features)
        total = 0
        genres = 0
        writers = 0
        length = 0
        parts = 0
        overAllSentiment = 0
        year = 0
        runtime = 0
        rating = 0
        ID = 0
        box = 0
        budget = 0
        for movie in data:
            total += 1
            for entry in data[movie]:
                try:
                    if entry == "genres":
                        genres += 1
                    elif entry == "writers":
                        writers += 1
                    elif entry == "length":
                        length += 1
                    elif entry == "parts":
                        parts += 1
                    elif entry == "overAllSentiment":
                        overAllSentiment += 1
                    elif entry == "Year":
                        year += 1
                    elif entry == "Runtime":
                        runtime += 1
                    elif entry == "imdbRating":
                        rating += 1
                    elif entry == "imdbID":
                        ID += 1
                    elif entry == "BoxOffice":
                        box += 1
                    elif entry == "Budget":
                        budget += 1
                    else:
                        pass
                except:
                    pass
        print("Total: %s \n Genres: %s \n Writers: %s \n Length: %s \n Parts: %s \n overAllSentiment %s \n year: %s \n Runtime: %s \n imdbRating: %s \n imdbID: %s \n BoxOffice: %s \n Budget: %s  " %
        (total, genres, writers, length, parts, overAllSentiment, year, runtime, rating, ID, box, budget))


# dont print but write to file this time
def makeSmolJsons():
    with open("./features/features.json", "r+") as features:
        data = json.load(features)
        genres = ""
        writers = ""
        length = ""
        parts = ""
        overAllSentiment = ""
        year = ""
        runtime = ""
        rating = ""
        ID = ""
        box = ""
        budget = ""
        for movie in data:
            for entry in data[movie]:
                try:
                    if entry == "genres":
                        for genre in data[movie][entry]:
                            genres += "%s;%s\n" % (movie, genre)
                    elif entry == "writers":
                        for writer in data[movie][entry]:
                            writers += "%s;%s\n" % (movie, writer)
                    elif entry == "length":
                        length += "%s;%s\n" % (movie, data[movie][entry])
                    elif entry == "parts":
                        parts += "%s;1;polarity;%s\n" % (movie, data[movie][entry]["1"]["sentiment"][0])
                        parts += "%s;1;subjectivity;%s\n" % (movie, data[movie][entry]["1"]["sentiment"][1])

                        parts += "%s;2;polarity;%s\n" % (movie, data[movie][entry]["2"]["sentiment"][0])
                        parts += "%s;2;subjectivity;%s\n" % (movie, data[movie][entry]["2"]["sentiment"][1])
                        
                        parts += "%s;3;polarity;%s\n" % (movie, data[movie][entry]["3"]["sentiment"][0])
                        parts += "%s;3;subjectivity;%s\n" % (movie, data[movie][entry]["3"]["sentiment"][1])
                        
                        parts += "%s;4;polarity;%s\n" % (movie, data[movie][entry]["4"]["sentiment"][0])
                        parts += "%s;4;subjectivity;%s\n" % (movie, data[movie][entry]["4"]["sentiment"][1])
                        
                        parts += "%s;5;polarity;%s\n" % (movie, data[movie][entry]["5"]["sentiment"][0])
                        parts += "%s;5;subjectivity;%s\n" % (movie, data[movie][entry]["5"]["sentiment"][1])

                    elif entry == "overAllSentiment":
                        overAllSentiment += "%s;polarity;%s\n" % (movie, data[movie][entry][0])
                        overAllSentiment += "%s;subjectivity;%s\n" % (movie, data[movie][entry][1])
                    elif entry == "Year":
                        year += "%s;%s\n" % (movie, data[movie][entry])
                    elif entry == "Runtime":
                        runtime += "%s;%s\n" % (movie, data[movie][entry])
                    elif entry == "imdbRating":
                        rating += "%s;%s\n" % (movie, data[movie][entry])
                    elif entry == "imdbID":
                        ID += "%s;%s\n" % (movie, data[movie][entry])
                    elif entry == "BoxOffice":
                        box += "%s;%s\n" % (movie, data[movie][entry])
                    elif entry == "Budget":
                        budget += "%s;%s\n" % (movie, data[movie][entry])
                    else:
                        pass
                except:
                    pass
        with open("./features/featuresGenre.csv", "w") as fGenre:
            fGenre.write(genres)
        with open("./features/featuresWriters.csv", "w") as fWriters:
            fWriters.write(writers)
        with open("./features/featuresLength.csv", "w") as fLength:
            fLength.write(length)
        with open("./features/featuresParts.csv", "w") as fParts:
            fParts.write(parts)
        with open("./features/featuresOverAllSentiment.csv", "w") as fallSent:
            fallSent.write(overAllSentiment)
        with open("./features/featuresYear.csv", "w") as fYear:
            fYear.write(year)
        with open("./features/featuresRuntime.csv", "w") as fRuntime:
            fRuntime.write(runtime)
        with open("./features/featuresRating.csv", "w") as fRating:
            fRating.write(rating)
        with open("./features/featuresID.csv", "w") as fID:
            fID.write(ID)
        with open("./features/featuresBoxOffice.csv", "w") as fBox:
            fBox.write(box)
        with open("./features/featuresBudget.csv", "w") as fBudget:
            fBudget.write(budget)

# reformatJson()
# checkAttributeCount()
makeSmolJsons()
