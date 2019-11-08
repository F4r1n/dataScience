import requests
import bs4


def featureToFile(movieString, response):
    print("Test")

with open("list.txt", 'r') as list:
        #iterate file line by line
        for movie in list:
            #replace blank spaces with - to use in the url
            movieString = movie.replace(" ", "-")
            #replace newlines for formatting
            movieString = movieString.replace("\n", "")
            #replace : because its not used by the site in the url
            movieString = movieString.replace(":", "")

            movieStringForURL = movie.replace(" ", "%%20")
            #replace newlines for formatting
            movieStringForURL = movieString.replace("\n", "")

            #request the page with the script
            res = requests.get(
                'https://www.imsdb.com/Movie%%20Scripts/%s%%20Script.html' % movieStringForURL)
            #if okay call function that saves the script
            if res.ok:
                featureToFile(movieString, res.text)
