#SOMETHING BROKE - script was used to extract the sentiment

# Data Preprocessing and Feature Engineering
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

import nltk
import os
import json
import wordcloud
import matplotlib.pylab as plt
from collections import Counter

nltk.download('stopwords')
# Get a list of stopwords from nltk
stopwords = nltk.corpus.stopwords.words("english")


def get_clean_words(words):
    def _isnum(w):
        try:
            int(w)
            return True
        except ValueError:
            return False

    # Set words to lowercase and remove them if they are stop words
    words = [w.lower() for w in words if w.lower() not in stopwords]

    # Remove punctuation
    words = [w.replace('(', '') for w in words]
    words = [w.replace(')', '') for w in words]
    words = [w.replace('?', '') for w in words]
    words = [w.replace(',', '') for w in words]
    words = [w.replace('.', '') for w in words]
    words = [w.replace('"', '') for w in words]
    words = [w.replace('!', '') for w in words]

    # Remove numbers
    words = [w for w in words if not _isnum(w)]

    # Only keep words with more than one character
    words = [w for w in words if len(w) > 1]

    return words


def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def word_count(text):
    return Counter(text.split())


movies = []
file_words = []

with open("features.json", "r+") as jsonFile:
    # data = json.load(jsonFile)
    with open("list.txt", 'r') as list:
        for movie in list:
            movie = movie.replace("\n", "")
            # replace blank spaces with - to use in the url
            movieString = movie.replace(" ", "-")
            # replace : because its not used by the site in the url
            movieString = movieString.replace(":", "")
            try:
                with open('./data/' + movieString + ".txt", "r") as file:
                    script = file.read().replace('\n', '')
                    words = script.split()
                    file_words.append(words)
                    movies.append(movie)
                    # Split movie script into five even parts
                    # movieParts = chunkIt(words, 5)
                    # data[movie]["parts"] = {}
                    # for i, moviePart in enumerate(movieParts):
                    #     textblob = TextBlob(' '.join(moviePart))
                    #     partSentiment = textblob.sentiment
                    #     data[movie]["parts"][str(i + 1)] = {}
                    #     data[movie]["parts"][str(
                    #         i + 1)]["sentiment"] = partSentiment
                    # scriptBlob = TextBlob(script)
                    # data[movie]["overAllSentiment"] = scriptBlob.sentiment
            except:
                print("Movie not found")
    # jsonFile.seek(0)
    # json.dump(data, jsonFile, indent=4)
    # jsonFile.truncate()

corpus = {}
word_counts = []
for m in movies:
    corpus[m] = []
for s, m in list(zip(file_words, movies)):
    clean_words = get_clean_words(s)
    corpus[m].append(' '.join(clean_words))
for m in corpus:
    corpus[m] = ' '.join(corpus[m])

with open('movies.csv', 'w') as f:
    for key in corpus.keys():
        my_dict = word_count(corpus[key])
        for k in my_dict.keys():
            if my_dict(k) > 6:
                f.write("%s,%s,%s\n" % (key, k, my_dict[k]))


# i = 0
# for t in corpus:
#     print(t)
#     fig = plt.figure(figsize=(12, 18))
#     plt.title(albums[t])
#     wc = wordcloud.WordCloud(
#         max_font_size=40, collocations=False).generate(corpus[t])
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     fig.savefig(albums[t] + '.png')
#     i += 1
