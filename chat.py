from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai


load_dotenv() #loading all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_response(question):
    response = model.generate_content(question)
    return response.text

#Initialize a Streamlit App

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")


if submit:
    response = get_response(input)
    st.subheader("The response is ...")
    st.write(response)