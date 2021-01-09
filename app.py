import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.title("The Conclusion of @realDonaldTrump")
st.subheader("A visualization of Trump's tweets between Election Day (11/03/2020) and the permanent ban of @realDonaldTrump (1/8/2021).")

@st.cache
def load_data():
    data = pd.read_csv('data/processed_tweets.csv',
    header=0)
    return data    

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data... done!')

st.write(data)

sentiment_subjectivity_chart = alt.Chart(data).mark_circle().encode(
    x='subjectivity',
    y='sentiment',
    tooltip='tweet_text'
).interactive()

st.write(sentiment_subjectivity_chart)

sentiment_timeline_chart = alt.Chart(data).mark_line().transform_window(
    rolling_mean='mean(sentiment)',
    frame=[-50, 50]
).encode(
    x = 'created_date:T',
    y='rolling_mean:Q'
)

st.write(sentiment_timeline_chart)