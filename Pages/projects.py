import streamlit as st 

st.title("Projects ")
col1, col2 , col3 = st.columns(3)
def container(title,image,date,description):
    c = st.container(border=1)
    c.write(title)
    c.image(image)
    c.write(date)
    with c.popover("Project Description"):
        st.write(description)
with col1:
    container("hello","./assets/me.jpeg","2024/2/1",description="hello world")
with col2:
    container("hello","./assets/me.jpeg","2024/2/1",description="pest pest")
with col3:
    container("hello","./assets/me.jpeg","2024/2/1",description="alllo ")