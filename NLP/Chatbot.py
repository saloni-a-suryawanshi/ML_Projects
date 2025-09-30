import streamlit as st

from nltk.chat.util import Chat,reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, how are you today?"]
    ],
    [
        r"(.*)your name(.*)",
        ["I am your friendly chatbot 🤖", "You can call me Chatty!"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you(.*)",
        ["I’m doing great, thanks! 😊", "I’m fine, how about you?"]
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
        r"(.*)love(.*)",
        ["Love is the most beautiful thing in world "]
    ],
   [
        r"(.*)Humans(.*)",
        ["Humans are the intelligent one on this planet but they don't use thier brain in any situation they always react wrong"]
    ],
   [
        r"(.*)Dog(.*)",
        ["Dogs are loyal and cute"]
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
         r"(.*)Pakistan(.*)",
        ["One of the galich country in the world . they don't have sense about how to speak and how to act infornt of other people. don't have sufficient food to eat,So don't visit there country this is my humble request"]       
    ],
    [
         r"(.*)womens(.*)",
        ["Women are important members of society who work, take care of families, and help lead communities."]
    ],
    [
         r"(.*)mens(.*)",
        ["Men are members of society who work, protect, and contribute to families and communities"]
    ],   
]


# Create chatbot
chat = Chat(pairs, reflections)

# Streamlit UI
st.title("💬 Chatbot using NLTK + Streamlit")

user_input = st.text_input("You: ", "")

if user_input:
    response = chat.respond(user_input)
    if response:
        st.text_area("Chatbot:", value=response, height=100)
    else:
        st.text_area("Chatbot:", value="Sorry, I didn’t understand that 🤔", height=100)


