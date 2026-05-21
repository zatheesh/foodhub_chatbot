
import streamlit as st
from foodhub_chatbot import chatagent

st.set_page_config(
    page_title="FoodHub Chatbot",
    page_icon="🍔"
)

st.title("🍔 FoodHub Customer Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I’m FoodHub Assistant. How can I help you today?"
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Example: Where is my order O12488?")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Checking FoodHub records..."):
            response = chatagent(user_input)

        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
