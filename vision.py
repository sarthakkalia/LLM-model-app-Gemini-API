from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(image, input):
    if(input!=""):
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)

    return response.text


st.set_page_config(page_title="Gemini Image Demo")
st.header('Gemini Application')

uploaded_file=st.file_uploader("Choose an Image... ",type=['jpg','jpeg','png'])
input=st.text_input("Input: ",key="input")

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Upload Image.", use_column_width=True)


submit=st.button("Tell me about the image")


if submit:
    response= get_gemini_response(image,input)
    st.write(response)