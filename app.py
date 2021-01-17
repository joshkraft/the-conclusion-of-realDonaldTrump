import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import json

""" Data """

@st.cache
def load_data():
    data = pd.read_csv('data/processed_tweets.csv',
    header=0, index_col=0)
    return data 

def generate_top_terms_df():
    file_names = ['locations', 'organizations', 'people']

    top_terms_df = pd.DataFrame()

    for file_name in file_names:
        with open('data/' + file_name + '.json', 'r') as f:
            data = json.load(f)
            temp_df = pd.DataFrame(data.items())
            temp_df[2] = file_name
            top_terms_df = top_terms_df.append(temp_df)

    top_terms_df.columns = ['Term', 'Mentions', 'Category']

    return top_terms_df

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


def phrase_bar_chart(data):
    phrase_bar_chart = alt.Chart(data).mark_bar().encode(
        x = 'count',
        y = alt.Y(
            'phrase', 
            sort = alt.EncodingSortField('count', order="descending"),
            axis = alt.Axis(labelAngle=0)),
    ).properties(
        width = 700
    )

    return phrase_bar_chart
"""
def generate_top_terms_chart(data):
    top_terms_chart = alt.Chart(data).mark_bar().encode(
        x = alt.X('Term', sort = alt.EncodingSortField('Mentions', order = "descending")),
        y = 'Mentions',
        color = 'Category:N',
        column = 'Category:N'
        )

    return top_terms_chart"""


def generate_top_terms_chart(data):
    top_terms_chart = alt.Chart(data, width=200, height = 1000).mark_text().encode(
        text = 'Term:N',
        x = alt.X(
            'jitter:Q',
            title = None,
            axis = alt.Axis(values=[0], ticks = True, grid = False, labels = False)),
        y = alt.Y('Mentions:Q'),
        color = alt.Color('Category:N'),
        column = alt.Column(
            'Category:N',
            header = alt.Header(
                labelAngle = 0,
                titleOrient = 'top', 
                labelOrient = 'bottom',
                labelAlign = 'center',
                labelPadding = 3
            ),
        ),
        opacity = 'Mentions:Q'
    ).transform_calculate(
        jitter='sqrt(-2*log(random()))*cos(2*PI*random())'
    ).configure_facet(
        spacing = 0
    ).configure_view(
        stroke = None
    )


    return top_terms_chart 

""" Page Rendering """

st.title("The Conclusion of @realDonaldTrump")
st.subheader("A visualization of Trump's tweets between Election Day (11/03/2020) and the permanent ban of @realDonaldTrump (1/8/2021).")
  

data = load_data()


st.subheader("During this time, @readlDonaldTrump tweeted " + str(len(data)) + " times, excluding retweets and link-only tweets.")
st.write(tweet_frequency_chart())

st.subheader("Using NLP, we can extract the topics that @realDonaldTrump tweeted about the most:")

st.write('To dig in further, select a topic:')
st.write('@realDonaldTrump was tweeting about.')

# filtered_tweets = data["tweet_text"].loc[data["tweet_text"].str.contains(topic_selection, case=False)]


#filtered_tweets = data.loc[data["tweet_text"].str.contains(topic_selection, case=False)]
#filtered_tweets['tweet_text']





st.title("Notes")
st.write("Retweets, and tweets containing only links have been removed.")



top_terms_df = generate_top_terms_df()

st.write(generate_top_terms_chart(top_terms_df))






"""

I think its time to move on from streamlit to a jupyter notebook blog post.

Make a single select plot, where you click a word and then see the data. Maybe put a bubble chart on the top, with a fixed df on bottom?



"""

def random_plot(data):
    chart = alt.Chart(data).mark_circle().encode(
        x = alt.X('Mentions:Q'),
        color = 'Category:N',
        size = "Mentions"
    ).properties(
        width = 400
    )

    return chart

st.write(random_plot(top_terms_df))