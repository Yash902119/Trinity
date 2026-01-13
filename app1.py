import streamlit as st
st.title("Some basic commands in Streamlit")
name=st.text_input("Enter your name")
if st.button("Submit"):
    st.write("Hello, ",name)