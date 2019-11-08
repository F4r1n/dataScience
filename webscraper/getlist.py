import requests
import bs4

#request site with list of all scripts
res = requests.get('https://www.imsdb.com/all%20scripts/')
#if request was successfull
if res.ok:
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    #search for the table
    td = soup.select('td')
    #Each movie has a link
    titles = td[86].find_all('a')
    #open a file for the list
    with open("list.txt", "w") as file:
        #iterate over all the movies
        for movie in titles:
            movieName = movie.getText()
            #write to file
            file.write("%s\n" % movieName)
