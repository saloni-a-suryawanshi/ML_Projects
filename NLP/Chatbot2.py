import streamlit as st
import random
from nltk.chat.util import Chat, reflections

# Define chatbot pairs
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, how are you today?", "Nice to meet you %2! How’s your day going?"]
    ],
    [
        r"(.*)your name(.*)",
        ["I am your friendly chatbot 🤖", "You can call me Chatty!", "I’m Chatty, your AI friend!"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you(.*)",
        ["I’m doing great, thanks! 😊", "I’m fine, how about you?", "Awesome as always 🚀"]
    ],
    [
        r"(.*)love(.*)",
        ["Love is the most beautiful thing in the world ❤️", "Love makes life meaningful 💕"]
    ],
    [
        r"(.*)dog(.*)",
        ["Dogs are loyal and cute 🐶", "A dog is a man’s best friend 🐕"]
    ],
    [

        r"where are you from(.*)",
        ["I live on the internet ", "I come from the digital world "]
    ],
    [
        r"(.*)live in(.*)",
        ["Oh nice! %2 must be a wonderful place "]
    ],
   [
        r"(.*)who invented airplane(.*)",
        ["The Wright brothers, Orville and Wilbur Wright, invented the first successful airplane"]
    ],
   [
        r"(.*)mount everest(.*)",
        ["Mount Everest is the highest peak in the world , located between Nepal and China."]
    ],
   [
        r"(.*)largest country(.*)",
        ["Russia is the largest country in the world by area "]
    ],
   [
        r"(.*)dress of maharashtra(.*)",
        ["Traditional dress of Maharashtra is Saree for women and Dhoti-Kurta for men "]
    ],
   [
        r"(.*)festivals of india(.*)",
        ["India celebrates Diwali, Holi, Eid, Christmas, Pongal, Baisakhi, and many more"]
    ],
   [
        r"(.*)army(.*)",
        ["""The army is a nation’s military force trained for land-based defense and combat operations. 🪖\n 
It protects the country’s borders, maintains peace, and assists in disaster relief and humanitarian missi ons."""]
    ],
    [
         r"(.*)India(.*)",
        ["India is a vast and diverse country in South Asia, known for its rich history, culture, and traditions."]
    ],
    [
         r"(.*)womens(.*)",
        ["Women are important members of society who work, take care of families, and help lead communities."]
    ],
    [
         r"(.*)mens(.*)",
        ["Men are members of society who work, protect, and contribute to families and communities"]
    ], 
   [
        r"(.*)Humans(.*)",
        ["Humans are the intelligent one on this planet but they don't use thier brain in any situation they always react wrong"]
    ],
]

# Create chatbot
chat = Chat(pairs, reflections)

# Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("💬 Chatbot using NLTK + Streamlit")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Get response (choose random if multiple)
    response = chat.respond(user_input)
    if response:
        if isinstance(response, list):
            response = random.choice(response)
    else:
        response = "🤔 Sorry, I didn’t understand that. Can you rephrase?"

    # Save to history
    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("bot", response))

# Display chat history
for sender, message in st.session_state.history:
    if sender == "user":
        with st.chat_message("user"):
            st.markdown(message)
    else:
        with st.chat_message("assistant"):
            st.markdown(message)
