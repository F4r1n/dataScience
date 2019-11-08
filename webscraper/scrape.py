import bs4
import requests
import os

#scriptToFile takes the fileName and html and writes it to a file
def scriptToFile(name, text):
    #Open new file in data directory
    with open(os.getcwd() + "/data/%s.txt" % name, "w") as file:
        soup = bs4.BeautifulSoup(text, features="lxml")
        #search for pre element which holds the script
        pre = soup.select('pre')
        #some scripts start with the following string. It is not detected as html by bs4 thus we remove it manually
        if len(pre) > 0:
            filterPre = pre[0].getText().replace("""


    <b><!--
    </b>if (window!= top)
    top.location.href=location.href
    <b>// -->
    </b>""" , "")
            #write filtered element to file
            file.write(filterPre)

#open file to store errors in to review them manually
with open("errors.txt", 'a') as file:
    #open file containing the list of movies
    with open("list.txt", 'r') as list:
        #iterate file line by line
        for movie in list:
            #replace blank spaces with - to use in the url
            movieString = movie.replace(" ", "-")
            #replace newlines for formatting
            movieString = movieString.replace("\n", "")
            #replace : because its not used by the site in the url
            movieString = movieString.replace(":", "")
            #request the page with the script
            res = requests.get('https://www.imsdb.com/scripts/%s.html' % movieString)
            #if okay call function that saves the script
            if res.ok:
                scriptToFile(movieString, res.text)
            #on error write movie title to error file
            else:
                file.write(movie)
