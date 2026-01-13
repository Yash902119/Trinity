import streamlit as st
st.title("some basic commands like slider button etc")
age=st.slider("Enter your age",1,100)
city=st.selectbox("Select your city",["Pune","Mumbai","Ahmedabad","Delhi","Banglore"])
if st.button("show details"):
    st.write("Age",age)
    st.write("City",city)  
st.checkbox("I agree to the terms and conditions")  

