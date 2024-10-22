import streamlit as st 

st.title("Projects ")
col1, col2 = st.columns(2)
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
    container(title="Audio Extractor Web App ",image="./assets/audio-extractor.png",
              description="""
              With this simple web application, you can effortlessly extract 
              audio from videos. Just upload your video, and within seconds,
                download the audio directly to your device. This fast and efficient tool,
                  built using Python and the Streamlit framework, 
                  makes the process quick and easy. Visit the site to explore its features,
                    and don’t forget to share your experience with us!  """
                    ,button_status="ON",
                    url_project="https://audio-extractor.streamlit.app")

with col2:
    container("""
Control Your Equipment With Bluetooth Mobile App""","./assets/bluetooth.png",
              description="""Using your smartphone and Bluetooth connectivity, 
              you can control everything you want and make your home smart . turn on/off machines , lights , doors 
              and more & more . """,button_status="ON",
              url_project="https://github.com/Ala-Eddine-Jelassi/Control-Your-specific-equipment-with-Bluetooth-mobile-APP")

    