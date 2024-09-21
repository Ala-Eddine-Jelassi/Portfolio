import streamlit as st 
stcc = st.container(border=True)
def contact_container():
    with stcc :
        st.title("Send Me Message")
        first_name = st.text_input("First Name 👤 👇")
        email =  st.text_input("Email 📧  ")
        message = st.text_area("Your Message 👇")
        submit =st.button("Submit")
    if submit:
        print(first_name,email,message)