import pandas as pd 

def load_data(filepath):
    data = pd.read_csv(filepath, header=0, index_col=0)
    return data

tweet_df = load_data('data/processed_tweets.csv')

def main():
    tweet_df = load_data('data/processed_tweets.csv')
    print(tweet_df)

if __name__ == "__main__":
    main()