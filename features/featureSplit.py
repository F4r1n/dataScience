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
        genres = {}
        writers = {}
        length = {}
        parts = {}
        overAllSentiment = {}
        year = {}
        runtime = {}
        rating = {}
        ID = {}
        box = {}
        budget = {}
        for movie in data:
            for entry in data[movie]:
                try:
                    if entry == "genres":
                        genres[movie] = data[movie][entry]
                    elif entry == "writers":
                        writers[movie] = data[movie][entry]
                    elif entry == "length":
                        length[movie] = data[movie][entry]
                    elif entry == "parts":
                        parts[movie] = data[movie][entry]
                    elif entry == "overAllSentiment":
                        overAllSentiment[movie] = data[movie][entry]
                    elif entry == "Year":
                        year[movie] = data[movie][entry]
                    elif entry == "Runtime":
                        runtime[movie] = data[movie][entry]
                    elif entry == "imdbRating":
                        rating[movie] = data[movie][entry]
                    elif entry == "imdbID":
                        ID[movie] = data[movie][entry]
                    elif entry == "BoxOffice":
                        box[movie] = data[movie][entry]
                    elif entry == "Budget":
                        budget[movie] = data[movie][entry]
                    else:
                        pass
                except:
                    pass
        with open("./features/featuresGenre.json", "w") as fGenre:
            jsonGenre = json.dumps(genres)
            fGenre.write(jsonGenre)
        with open("./features/featuresWriters.json", "w") as fWriters:
            jsonWriters = json.dumps(writers)
            fWriters.write(jsonWriters)
        with open("./features/featuresLength.json", "w") as fLength:
            jsonLength = json.dumps(length)
            fLength.write(jsonLength)
        with open("./features/featuresParts.json", "w") as fParts:
            jsonParts = json.dumps(parts)
            fParts.write(jsonParts)
        with open("./features/featuresOverAllSentiment.json", "w") as fallSent:
            jsonSentiment = json.dumps(overAllSentiment)
            fallSent.write(jsonSentiment)
        with open("./features/featuresYear.json", "w") as fYear:
            jsonYear = json.dumps(year)
            fYear.write(jsonYear)
        with open("./features/featuresRuntime.json", "w") as fRuntime:
            jsonRuntime = json.dumps(runtime)
            fRuntime.write(jsonRuntime)
        with open("./features/featuresRating.json", "w") as fRating:
            jsonRating = json.dumps(rating)
            fRating.write(jsonRating)
        with open("./features/featuresID.json", "w") as fID:
            jsonID = json.dumps(ID)
            fID.write(jsonID)
        with open("./features/featuresBoxOffice.json", "w") as fBox:
            jsonBox = json.dumps(box)
            fBox.write(jsonBox)
        with open("./features/featuresBudget.json", "w") as fBudget:
            jsonBudget = json.dumps(budget)
            fBudget.write(jsonBudget)

# reformatJson()
# checkAttributeCount()
makeSmolJsons()
