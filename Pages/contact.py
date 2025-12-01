import streamlit as st 




st.title("Contact ")
st.write("Social Media Network ")
col1 , col2 , col3, col4 = st.columns(4)
with col1:
    twitter_button = st.link_button("Twitter ","https://x.com/AlaDDin_JL")
with col2:
    linkedin_button = st.link_button("Linkedin ","https://www.linkedin.com/in/aladinjelassi/")
with col3:
    facebook_button = st.link_button("Facebook ","https://www.Facebook.com")
with col4:
    all_links = st.link_button("All Links","https://alfan.link/barcode")
st.write('')

stcc = st.container(border=True)
with stcc :
    st.title("Send Me Message")
    first_name = st.text_input("First Name 👤 👇")
    email =  st.text_input("Email 📧  ")
    message = st.text_area("Your Message 👇")
    submit =st.button("Submit")

   
       


