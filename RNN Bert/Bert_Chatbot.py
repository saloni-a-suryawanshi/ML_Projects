import streamlit as st
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import base64

# Adding background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call the function to set the background
set_background(r"C:\Users\Saloni\Desktop\HAPPY+SAD\draw2.jpg")

# Load BERT tokenizer and model
@st.cache_resource
def load_bert_model():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    return tokenizer, model

tokenizer, model = load_bert_model()

# Predefined questions and responses
qa_pairs = {
    "What is BERT?": "BERT stands for Bidirectional Encoder Representations from Transformers. It is a model developed by Google to help computers understand the meaning of language in context.",
    "Who developed BERT and when?": "BERT was developed by researchers at Google AI Language and introduced in October 2018.",
    "What makes BERT different from other NLP models?": "BERT reads text in both directions — left-to-right and right-to-left — giving it a deeper understanding of context compared to earlier models.",
    "What is the architecture of BERT?": "BERT is based on the Transformer encoder architecture, which uses self-attention mechanisms to process all words in a sentence simultaneously.",
    "What are the main versions of BERT?": "There are two main versions: BERT Base with 12 layers and 110 million parameters, and BERT Large with 24 layers and 340 million parameters.",
    "What are the training objectives of BERT?": "BERT is trained using Masked Language Modeling (MLM) and Next Sentence Prediction (NSP) to understand word meanings and sentence relationships.",
    "What are embeddings in BERT?": "BERT creates contextual embeddings, meaning each word’s representation depends on its surrounding words, allowing it to capture meaning accurately.",
    "How is BERT fine-tuned for tasks?": "After pre-training, BERT can be fine-tuned on specific NLP tasks like text classification, question answering, or sentiment analysis by adding task-specific layers.",
    "What are the applications of BERT?": "BERT is used in chatbots, search engines, sentiment analysis, question answering, and text summarization tasks.",
    "What are the limitations of BERT?": "BERT requires large computational resources, has a 512-token input limit, and may overfit when fine-tuned on small datasets."
}

# Function to get BERT embeddings
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

# Precompute embeddings for predefined questions
predefined_embeddings = {question: get_bert_embedding(question) for question in qa_pairs}

# Function to get the chatbot's response
def chatbot_response(user_input):
    user_embedding = get_bert_embedding(user_input)
    similarities = {
        question: cosine_similarity(user_embedding, predefined_embeddings[question])[0][0]
        for question in qa_pairs
    }
    best_match = max(similarities, key=similarities.get)
    if similarities[best_match] > 0.5:
        return qa_pairs[best_match]
    else:
        return "I'm not sure how to respond to that."

# Streamlit UI
st.title(" BERT Chatbot")
st.write("Ask me anything about BERT — I'm powered by a transformer model!")
user_input = st.text_input("You:", placeholder="Type your question here...")

if user_input:
    response = chatbot_response(user_input)
    st.write(f"**Chatbot:** {response}")

st.markdown("---")
