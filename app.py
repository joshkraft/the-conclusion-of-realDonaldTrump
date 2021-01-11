import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

""" Data """

@st.cache
def load_data():
    data = pd.read_csv('data/processed_tweets.csv',
    header=0, index_col=0)
    return data  


""" Charts """

def tweet_frequency_chart():
    frequency_chart = alt.Chart(data).mark_bar().encode(
        x='created_date:T',
        y='count()',
        tooltip='count()'
    ).interactive().properties(
        width=700
    )

    return frequency_chart

def sentiment_and_subjectivity_chart():
    sentiment_and_subjectivity_chart = alt.Chart(data).mark_circle().encode(
        x='subjectivity',
        y='sentiment',
        tooltip='tweet_text'
    ).interactive().properties(
        width=700
    )

    return sentiment_and_subjectivity_chart

def sentiment_timeline_chart():
    sentiment_timeline_chart = alt.Chart(data).mark_line().transform_window(
        rolling_mean='mean(sentiment)',
        frame=[-50, 50]
    ).encode(
        x = 'created_date:T',
        y='rolling_mean:Q'
    ).properties(
        width=700
    )

    return sentiment_timeline_chart




""" Page Rendering """

st.title("The Conclusion of @realDonaldTrump")
st.subheader("A visualization of Trump's tweets between Election Day (11/03/2020) and the permanent ban of @realDonaldTrump (1/8/2021).")
  

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data... done!')

st.write(data)
st.title("Frequency of Tweets")
st.write(tweet_frequency_chart())

st.title("Sentiment vs Subjectivity")
st.write(sentiment_and_subjectivity_chart())

st.title("Sentiment Timeline")
st.write(sentiment_timeline_chart())

st.title("Notes")
st.write("Retweets, and tweets containing only links have been removed.")
