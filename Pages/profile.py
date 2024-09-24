import streamlit as st 
from widgets.contactme import Qr_contact


col1,col2 = st.columns(2)
with col1:
    st.image("./assets/me.png")
with col2:
    st.title('ALAEDDIN JELASSI')
    st.write("ELECTRICAL ENGINEERING STUDENT")
    if st.button(" ✉️ Contact Me",type="primary"):
       Qr_contact()
st.title("Education")
st.write("""
- Master Degree Artificial Intelligence and Innovation Management (Future Plan )
- Bachelor Automation Engineering ( Not finished yet )
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