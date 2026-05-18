import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="AI Sentiment Chatbot")

st.title("AI Sentiment Chatbot")

st.write("Chat with the bot and detect emotions in real time!")

# Chat input
user_input = st.chat_input("enter your text here")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Sentiment analysis
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    # Bot response
    if polarity > 0:
        response = "You seem happy today:) Keep smiling!"
    elif polarity < 0:
        response = "I'm sorry you're feeling low :(. Hope things get better!"
    else:
        response = "Hmm... feeling neutral today :/"

    # Show bot message
    with st.chat_message("assistant"):
        st.write(response)
        