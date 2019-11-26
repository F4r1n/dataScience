#Data Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Data Preprocessing and Feature Engineering
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#Model Selection and Validation
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

import re
import nltk
import os
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
    
    
def word_count(text):
    return Counter(text.split())

movies = []
file_words = []
for filename in os.listdir('./data/'):
    movie = filename.replace('.txt', '')
    movies.append(movie)
    with open('./data/' + filename, "r") as file:
        data = file.read().replace('\n', '')
        words = data.split()
        file_words.append(words)

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
        # print(key, my_dict["love"])
        for k in my_dict.keys():
            f.write("%s,%s,%s\n"%(key,k,my_dict[k]))


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
