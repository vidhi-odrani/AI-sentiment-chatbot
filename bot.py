import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis Bot")

user_input=st.text_input("Enter your message")
if user_input:
    analysis=TextBlob(user_input)
    sentiment=analysis.sentiment.polarity
    
    if sentiment>0:
        st.write("Positive Sentiment")
    elif sentiment<0:
        st.write("Negative Sentiment")
    else:
        st.write("Neutral Sentiment")

        st.write("detected sentiment:", sentiment)
        