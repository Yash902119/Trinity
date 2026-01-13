
import streamlit as st  
st.title("Simple Calculator")
num1=st.number_input("Enter first number")
num2=st.number_input("Enter second number")
operation=st.selectbox("Select operation",["Add","Subtract","Multiply","Divide"])
if st.button("calculate"):
    if operation=="Add":
        result=num1+num2
        st.write("Result:",result)
    elif operation=="Subtract":
        result=num1-num2
        st.write("Result:",result)
    elif operation=="Multiply":
        result=num1*num2
        st.write("Result:",result)
    elif operation=="Divide":
        result=num1/num2
        st.write("Result:",result)
graph=st.checkbox("Show Graph")
if graph:   
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.array([1,2,3,4,5])
    y=num1*x+num2
    plt.plot(x,y)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Graph of Y={}*X + {}".format(num1,num2))
    st.pyplot(plt)
    