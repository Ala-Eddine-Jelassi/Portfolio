import streamlit as st 

st.title("Introduction : ")
st.write("In this Section i Introduce My Ideas and My Future Ideas as well . ")

def container(title,image,description,url,url_title):#// c = st.container(border=1)
    with st.expander(title,expanded=True):
        col1 , col2 = st.columns(2)
        with col1:
            st.image(image)
        with col2:
            st.title(title)
            st.write(description)
            if url_title == "No":
                st.write('')
            else:
                st.link_button(url_title,url)
container("Giulianna","./assets/Home_Assistante.png",""""Giulianna it's A
           Home Assistante Crossplatfrom Application . 
          It is a idea that  can create the difference and 
          can go away with the iot and home acces controller . 
          this app created with flutter and dart programming langage also i 
          used mongodb and supabase as backend services and other tools like MQTT ... . 
          the project also combine Hardware compoments in this case i used ESP32 and sensors, 
          (Not finished Yet )""","https://youtu.be/2G75Hy9w2YI?si=Dqe84GdLodo6G-0f",url_title="Youtube Video")

container("My Home Controller","./assets/Nodered_dashboard.png","""
My Home Controller is an IOT (Internet Of Things) Project that allow you to controller your home devices 
(Washing Machine , TV , Doors ...) from a Node-RED Dashboard from anywere in the world , you can acces to the platfrom locally ( LAN : Local Area Network)
or via Your Smart Phone using the Node-RED Mobile Application or with the a Network IP Adress . 
this Project Has Benefits Mesure Temperature , Humidity and Gas after thzt store the data into 
          SQL Database also in CSV file also if you Need The Resume the System Will Send you 
          an email with csv file contain all data you need it . (Not Finished Yet )
""","https://www.linkedin.com/posts/aladinjelassi_iot-homeautomation-nodered-activity-7249119307333259264-alob?utm_source=share&utm_medium=member_desktop","Linkedin Post")

container("Water Pump Controller","./assets/water_pump.png","""
In our days, water is a treasure. We should use it correctly and carefully.
 To address this, I invented a solution to use water more efficiently than before:
 a small box with three components (a microcontroller, a SIM module, and a battery or power supply).

This project allows users to open or close the water from anywhere in the world with just an SMS.
 For example, you can open the water in the field or garden for animals anytime and anywhere with just a short message.
 This project helps us save time, money, and provides convenience. The box is easy to install and is affordable. ( Finished )
          
""","https://drive.google.com/drive/my-drive","No")
