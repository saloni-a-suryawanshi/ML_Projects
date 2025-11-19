import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# ✅ Configure API key
os.environ['GEMINI_API_KEY'] = "AIzaSyDOaVgRYz1q031aJadm2SjMOGFBfYCgVjc"
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# ✅ Streamlit setup
st.set_page_config(page_title="Image to Text Generator", layout="centered")
st.header("🧠 Gemini AI Image Analyzer")

# ✅ User input
input_prompt = st.text_input("Enter your prompt (optional):", key="input")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

if st.button("🔍 Analyze Image"):
    if image is None:
        st.warning("⚠️ Please upload an image first.")
    else:
        try:
            model = genai.GenerativeModel("models/gemini-2.0-flash")
            if input_prompt:
                response = model.generate_content([input_prompt, image])
            else:
                response = model.generate_content(image)

            st.subheader("✅ Response:")
            st.write(response.text)

        except Exception as e:
            st.error(f"🚨 Error: {e}")
