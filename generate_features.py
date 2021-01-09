import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob
import collections
import itertools
import re
import datetime

def load_raw_data(filepath):
    data = pd.read_csv(filepath, header=0, index_col=0)
    return data


def write_csv(df, filename):
    df.to_csv('data/' + filename, header=True)


def extract_n_most_frequent_words(tweets, n):
    stop_words = set(stopwords.words('english'))
    words_list = []

    for column, tweet in tweets.iterrows():
        split_text = split_tweet_text(tweet)
        words_list.append(split_text)

    flattened_words_list = list(itertools.chain(*words_list))
    words_without_stopwords = [word for word in flattened_words_list if not word in stop_words]
    word_counts = collections.Counter(words_without_stopwords).most_common(n)

    return pd.DataFrame(word_counts, columns=['word','times_used'])


def split_tweet_text(tweet):
    tweet_text = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", 
                tweet['tweet_text']).split())
    return tweet_text.lower().split()

def generate_sentiment_score(df):
    df['sentiment'] = df['tweet_text'].apply(lambda tweet: TextBlob(tweet).sentiment.polarity)
    return df

def generate_subjectivity_score(df):
    df['subjectivity'] = df['tweet_text'].apply(lambda tweet: TextBlob(tweet).sentiment.subjectivity)
    return df

def generate_date_columns(df):
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['created_at_est'] = df['created_at'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
    df['created_date'] = df['created_at_est'].apply(lambda datetime: datetime.date())
    return df


def main():
    tweet_df = load_raw_data('data/raw_tweets.csv')
    tweet_df = generate_sentiment_score(tweet_df)
    tweet_df = generate_subjectivity_score(tweet_df)
    tweet_df = generate_date_columns(tweet_df)
    write_csv(tweet_df, 'processed_tweets.csv')

    most_frequent_words = extract_n_most_frequent_words(tweet_df, 20)
    write_csv(most_frequent_words, 'word_frequency.csv')



if __name__ == '__main__':
    main()
    

