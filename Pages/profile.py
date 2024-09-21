import streamlit as st 



col1,col2 = st.columns(2)
with col1:
    st.image("https://media.licdn.com/dms/image/v2/C4E03AQFSiwNI_CefJw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1652455460179?e=1732147200&v=beta&t=JtKc3vvZzAKuR1lsDGs7ghAPyOuHhdbpXv2znXgr4fk",width=250)
with col2:
    st.title('ALAEDDIN JELASSI')
    st.write("ELECTRICAL ENGINEERING STUDENT")
    st.button(" ✉️ Contact Me",type="primary")
st.title("Education")
st.write("""
- Master Degree Artificial Intelligence and Innovation Management
- Bachelor Automation Engineering
""")
st.title("Hard Skills")
st.write("""
- Programming : Python , Dart , C/C++ , LD , SQL
- Boards : Raspberry pi ,ESP32 , Arduino , Nodemcu 
- Software : Tia Portal , Vs Code , Android Studio , Xcode , Arduino IDE , Fritzing , Thonny IDE , Xrelais , Matlab
- Databases : MYSQL , MongDB 
- Others : Node-RED , MQTT , Webosocket 

""")
st.title("Languages")
st.write("""
- Arabic ( Native Language )
- Italian  ( Plida B2 )  
- French ( A2 )
- English ( A2 )    
""")