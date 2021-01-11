import pandas as pd
import re

data = pd.read_json('data/raw_tweets.json')

def drop_links_from_tweets(data):
    data['text'] = data['text'].apply(drop_link_from_text)
    return data

def drop_link_from_text(text):
    return re.sub(r"http\S+", "", text)

def drop_blank_tweets(data):
    return data[data.text != '']

def create_document_from_tweets(data):
    return " ".join(tweet for tweet in data.text)
    

def main():
    COLS = ['date', 'favorites', 'id', 'isRetweet', 'retweets', 'text']
    data = pd.read_json('data/raw_tweets.json')
    data = drop_links_from_tweets(data)
    data = drop_blank_tweets(data)
    data.to_csv('data/tweets_for_comprehend.csv')

    # Concat to one document
    document = create_document_from_tweets(data)
    document_file = open('data/tweet_document.txt', 'wt')
    output = document_file.write(document)
    document_file.close()


if __name__ == '__main__':
    main()