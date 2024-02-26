# Q&A Chatbot

from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    input_data = [input, image] if input else [image]
    response = model.generate_content(input_data)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Prasanna Image Description Application")

input_prompt = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit_button = st.button("Tell me about the image")

# If the submit button is clicked
if submit_button:
    response = get_gemini_response(input_prompt, image)
    st.subheader("The Response is")
    st.write(response)
