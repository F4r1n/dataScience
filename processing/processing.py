#Data Preprocessing and Feature Engineering
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

import nltk
import os
import wordcloud
import matplotlib.pylab as plt
from collections import Counter

nltk.download('stopwords')
# Get a list of stopwords from nltk
stopwords = nltk.corpus.stopwords.words("english")
#adding numbers because they are bloating the word counts
stopwords.append('one')
stopwords.append('two')
stopwords.append('three')
stopwords.append('four')
stopwords.append('five')
stopwords.append('six')
stopwords.append('seven')
stopwords.append('eight')
stopwords.append('nine')
stopwords.append('ten')
#remove pronouns and some other words
stopwords.append('he')
stopwords.append('she')
stopwords.append('it')
stopwords.append('we')
stopwords.append('you')
stopwords.append('they')
stopwords.append('him')
stopwords.append('her')
stopwords.append('hers')
stopwords.append('his')
stopwords.append('yours')
stopwords.append('mine')
stopwords.append('my')
stopwords.append('I\'m')
stopwords.append('I\'ll')
stopwords.append('that')
stopwords.append('me')
stopwords.append('will')
stopwords.append('make')

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
    
    
def word_count(text):
    return Counter(text.split())

movies = []
file_words = []
#opene ach file and count the words
for filename in os.listdir('./data/'):
    movie = filename.replace('.txt', '')
    movie = movie.replace('-', ' ')
    movies.append(movie)
    with open('./data/' + filename, "r") as file:
        data = file.read().replace('\n', '')
        words = data.split()
        file_words.append(words)

#organize the results in a dict
corpus = {}
word_counts = []
for m in movies:
    corpus[m] = []
for s, m in list(zip(file_words, movies)):
    clean_words = get_clean_words(s)
    corpus[m].append(' '.join(clean_words))
for m in corpus:
    corpus[m] = ' '.join(corpus[m])

#write the results to a file
with open('movies.csv', 'w') as f:
    for key in corpus.keys():
        my_dict = word_count(corpus[key])
        for k in my_dict.keys():
            if my_dict[k] > 8:
                f.write("%s;%s;%s\n" % (key, k, my_dict[k]))


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
