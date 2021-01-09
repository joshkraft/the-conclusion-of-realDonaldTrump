import streamlit as st
import numpy as np
import pandas as pd

st.title("The Conclusion of @realDonaldTrump")
st.subheader("A visualization of Trump's tweets between Election Day (11/03/2020) and the permanent ban of @realDonaldTrump (1/8/2021).")

@st.cache
def load_data():
    data = pd.read_csv('data/data.csv',
    header=0)
    return data    

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data... done!')

st.write(data)

for tweet in data['tweet_text'][-5:]:
    st.write(tweet)