import streamlit as st 

st.title("Projects ")
col1, col2 , col3 = st.columns(3)
def container(title,image,description,button_status,url_project):
    c = st.container(border=1)
    c.write(title)
    c.image(image)
    with c.popover("Project Description"):
        st.write(description)
    if button_status == "ON":
        c.link_button("Url Project",url_project)
    else:
        c.write("")
with col1:
    container("Auto-Devices","./assets/telegramBot.png",description="""With a Telegram Bot,
               you can do anythin you want, such as controlling home devices,
               monitoring systems, or even checking a weather station using your smartphone or computer.
               With just a short message, you can accomplish a lot . 
                """,button_status="OFF",url_project="")
with col2:
    container("""
Control Your Equipment With Bluetooth Mobile App""","./assets/bluetooth.png",
              description="""Using your smartphone and Bluetooth connectivity, 
              you can control everything you want and make your home smart . turn on/off machines , lights , doors 
              and more & more . """,button_status="ON",
              url_project="https://github.com/Ala-Eddine-Jelassi/Control-Your-specific-equipment-with-Bluetooth-mobile-APP")
#with col3:
   # container("hello","./assets/me.png","2024/2/1",
              #description="alllo ",button_status="OFF",url_project=" vccv")