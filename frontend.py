import streamlit as st
import requests

st.title("AI Chatbot 🤖")

st.write("Talk to an AI-powered chatbot!")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input})
        if response.status_code == 200:
            bot_reply = response.json()["reply"]
            st.text_area("Chatbot:", value=bot_reply, height=100)
        else:
            st.error("Error connecting to the chatbot API.")
