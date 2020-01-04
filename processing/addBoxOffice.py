import requests
import bs4
import re
import json


with open("features.json", "r+") as jsonFile:
    #load json object
    data = json.load(jsonFile)

    #iterate file
    for obj in data:
        try:
            #request the page with the information
            res = requests.get('https://www.imdb.com/title/%s/' % data[obj]["imdbID"])
            #if okay call function that saves the script
            print(obj)
            if res.ok:
                soup = bs4.BeautifulSoup(res.text, features="lxml")
                box = soup.find_all("h4", string="Cumulative Worldwide Gross:")
                budget = soup.find_all("h4", string="Budget:")
                if box:
                    box = box[0].next_element.next_element.strip()
                    data[obj]["BoxOffice"] = box
                else:
                    data[obj]["BoxOffice"] = "N/A"
                    
                if budget:
                    budget = budget[0].next_element.next_element.strip()
                    data[obj]["Budget"] = budget
                else:
                    data[obj]["Budget"] = "N/A"
        except:
            print("ERROR:" + obj)
    jsonFile.seek(0)
    json.dump(data, jsonFile, indent=4)
    jsonFile.truncate()
