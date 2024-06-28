from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


load_dotenv() #loading all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini model and get responses
model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

#Initialize a Streamlit App

st.set_page_config(page_title="Vision Demo")

st.header("Gemini Vision Application")

#input = st.text_input("Input Prompt : ",key="input")
#submit = st.button("Ask the question")

input='''Give a detailed summary about the book . If the image is not book .Ask the user to
 upload book image with the visibility of Book Title'''
uploaded_file = st.file_uploader("Choose an image..", type=["jpg", "jpeg", "png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell me about the Image.")

if submit:
    response = get_response(input,image)
    st.subheader("The response is ...")
    st.write(response)