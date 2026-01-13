import streamlit as st
import google.generativeai as genai
st.title("Chat with Generative AI")
user_input=st.text_input("Ask me anything")
genai.configure(api_key="AIzaSyCGEoHRopKXpHtegvY7GmAhk4eYxBMVZP8")
model =genai.GenerativeModel("models/gemini-2.5-flash")
if user_input:
    response= model.generate_content(user_input)
    st.write("Response",response.text)

