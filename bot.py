import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="AI Sentiment Chatbot")

st.title("AI Sentiment Chatbot")
st.write("Chat with the bot and detect emotions in real time!")

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

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

    elif "sad" in user_input.lower() or "depressed" in user_input.lower():
        response = "I'm sorry you're feeling down 😢 Remember, it's okay to ask for help." 
        
    elif "scared" in user_input.lower() or "anxious" in user_input.lower():
        response = "It sounds like you're feeling anxious 😟 Try some deep breathing exercises."

    elif "stress" in user_input.lower() or "tired" in user_input.lower():
        response = "Looks like you're stressed 😓 Make sure to rest."

    elif polarity > 0.5:
        response = "Wow! You're sounding super excited today 🤩"

    elif polarity > 0:
        response = "You seem happy today 😊 Keep smiling!"

    elif polarity < -0.5:
        response = "That sounds really upsetting 😔 Hope things improve soon."

    elif polarity < 0:
        response = "I'm sorry you're feeling low 😔"

    else:
        response = "Hmm... feeling neutral today 😐"

    # Store bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)