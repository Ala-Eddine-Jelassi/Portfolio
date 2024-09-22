import smtplib
import re
smtp_server = "smtp.gmail.com"
port = 587 # tls port 
email_sender = "alajlassi624@gmail.com"
password = "tlqd hxoz lphu wqsa"
subject = "Thank You For Sending You message "
body = " We will Contact You as soon as possible . "

def email_valid(recipient_email,name):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex,recipient_email):
        return send_email(recipient_email,name) 
    else:
        msg = "Check Your Email !"
        return msg 

    
def send_email(recipient_email, name):
    Newsubject = " Hello "+name+" "+subject
    email_message = f"Subject:{Newsubject}\n\n{body}"
    try :
        server = smtplib.SMTP(smtp_server,port)
        server.starttls()
        server.login(email_sender,password)
        server.sendmail(email_sender,recipient_email,email_message)
        info = "EmailSend"
        #print(info)
        return info
        
    except Exception as e :
        print(f"faild-----------------{e}")
    finally:
        print("finito")
        server.quit()


