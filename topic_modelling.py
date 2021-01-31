import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF



"""
Index(['Unnamed: 0', 'id', 'username', 'tweet_text', 'retweets', 'location',
       'created_at', 'sentiment', 'subjectivity', 'created_at_est',
       'created_date'],
      dtype='object')
"""


def read_tweets_to_df(filepath):
    return pd.read_csv(filepath)


tweets = read_tweets_to_df("data/processed_tweets.csv")



def doLDA():

    vectorizer = CountVectorizer(max_df = 0.8, min_df = 2, stop_words = 'english')

    doc_term_matrix = vectorizer.fit_transform(tweets['tweet_text'])

    LDA = LatentDirichletAllocation(n_components = 10, random_state = 42)
    LDA.fit(doc_term_matrix)
    """
    for i in range(10):
        rand_id = random.randint(0, len(vectorizer.get_feature_names()))
        #print(vectorizer.get_feature_names()[rand_id])

    first_topic = LDA.components_[0]
    print(first_topic)"""

    for i,topic in enumerate(LDA.components_):
        print(f'Top 10 words for topic #{i}:')
        print([vectorizer.get_feature_names()[i] for i in topic.argsort()[-10:]])
        print('\n')

def doNMF(tweets):
    tfidf_vectorizer = TfidfVectorizer(max_df = 0.9, min_df = 25, stop_words = 'english')
    doc_term_matrix = tfidf_vectorizer.fit_transform(tweets['tweet_text'])

    nmf = NMF(n_components=6, random_state = 42)
    nmf.fit(doc_term_matrix)

    for i, topic in enumerate(nmf.components_):
        print(f'Top 10 words for topic #{i}:')
        print([tfidf_vectorizer.get_feature_names()[i] for i in topic.argsort()[-10:]])
        print('\n')

doNMF(tweets)

"""At some point, I feel like I need to go back to PYLDAVIS..."""