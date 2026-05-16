import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# ---------------- FIREBASE INIT ----------------
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ---------------- UI ----------------
st.title("Contact ")
st.write("Social Media Network ")

col1 , col2 , col3, col4 = st.columns(4)

with col1:
    st.link_button("Twitter ", "https://x.com/AlaDDin_JL")
with col2:
    st.link_button("LinkedIn ", "https://www.linkedin.com/in/aladinjelassi/")
with col3:
    st.link_button("Facebook ", "https://www.Facebook.com")
with col4:
    st.link_button("All Links", "https://alfan.link/barcode")

st.write("")

stcc = st.container(border=True)

with stcc:
    st.title("Send Me Message")

    first_name = st.text_input("First Name 👤 👇")
    email = st.text_input("Email 📧")
    message = st.text_area("Your Message 👇")

    submit = st.button("Submit")

    if submit:
        if first_name and email and message:

            db.collection("messages").add({
                "first_name": first_name,
                "email": email,
                "message": message
            })

            st.success("Message sent successfully 🚀")

        else:
            st.error("Please fill all fields ❗")
