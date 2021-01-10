import pandas as pd 
import nltk

def load_data(filepath):
    data = pd.read_csv(filepath, header=0, index_col=0)
    return data

def clean_tweets(tweet_df):
    pass



def main():
    tweet_df = load_data('data/processed_tweets.csv')
    clean_tweets(tweet_df[:5])


    print(tweet_df['tweet_text'])

if __name__ == "__main__":
    main()