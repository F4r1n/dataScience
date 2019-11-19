import re
import nltk
import os
import wordcloud
import matplotlib.pylab as plt
from collections import Counter

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

corpus = {}
word_counts = []
for i in range(len(tags)):
    if tags[i] == 5 or tags[i] == 8:
        tags[i] = 4
for t in tags:
    corpus[t] = []
for s, t in list(zip(song_words, tags)):
    clean_words = get_clean_words(s)
    corpus[t].append(' '.join(clean_words))
for t in corpus:
    corpus[t] = ' '.join(corpus[t])

with open('mumford.csv', 'w') as f:
    for key in corpus.keys():
        my_dict = word_count(corpus[key])
        # print(key, my_dict["love"])
        for k in my_dict.keys():
            f.write("%s,%s,%s\n"%(albums[key],k,my_dict[k]))


i = 0
for t in corpus:
    print(t)
    fig = plt.figure(figsize=(12, 18))
    plt.title(albums[t])
    wc = wordcloud.WordCloud(
        max_font_size=40, collocations=False).generate(corpus[t])
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    fig.savefig(albums[t] + '.png')
    i += 1
