import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="AI Sentiment Chatbot")

st.title("AI Sentiment Chatbot")
st.write("Chat with the bot and detect emotions in real time!")

st.sidebar.title("🤖 Chatbot Controls")

clear_chat = st.sidebar.button("Clear Chat")

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if clear_chat:
    st.session_state.messages = []

    st.session_state.sentiment_count = {
        "Positive": 0,
        "Negative": 0,
        "Neutral": 0
    }
    
if "sentiment_count" not in st.session_state:
    st.session_state.sentiment_count = {
        "Positive": 0,
        "Negative": 0,
        "Neutral": 0
    }
# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Store and display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Sentiment analysis
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

        # Emotion responses
    if "angry" in user_input.lower():
        response = "You seem angry 😠 Try taking a short break."
        st.session_state.sentiment_count["Negative"] += 1

    elif "scared" in user_input.lower() or "anxious" in user_input.lower():
        response = "You seem worried 😟 Everything will be okay."
        st.session_state.sentiment_count["Negative"] += 1

    elif "stress" in user_input.lower() or "tired" in user_input.lower():
        response = "Looks like you're stressed 😓 Make sure to rest."
        st.session_state.sentiment_count["Negative"] += 1

    elif polarity > 0.5:
        response = "Wow! You're sounding super excited today 🤩"
        st.session_state.sentiment_count["Positive"] += 1

    elif polarity > 0:
        response = "You seem happy today 😊 Keep smiling!"
        st.session_state.sentiment_count["Positive"] += 1

    elif polarity < -0.5:
        response = "That sounds really upsetting 😔 Hope things improve soon."
        st.session_state.sentiment_count["Negative"] += 1

    elif polarity < 0:
        response = "I'm sorry you're feeling low 😔"
        st.session_state.sentiment_count["Negative"] += 1

    else:
        response = "Hmm... feeling neutral today 😐"
        st.session_state.sentiment_count["Neutral"] += 1

    # Store bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)

if len(st.session_state.messages) > 0:

    st.sidebar.subheader("📊 Sentiment Analytics")
    st.sidebar.bar_chart(st.session_state.sentiment_count)
