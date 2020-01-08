import json

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

#I wanted to check if and which elements are missing by counting and printing all the field
def checkAttributeCount():
    with open("./features/features.json", "r+") as features:
        data = json.load(features)
        genres = 0
        writers = 0
        length = 0
        parts = 0
        overAllSentiment = 0
        genres = 0
        for movie in data:
            for entry in data[movie]:
                print(entry)
            break;
            # data[movie]["title"] = movie
            # obj = json.dumps(data[movie])
            # new.write(obj + ",\n")

smallJsons()