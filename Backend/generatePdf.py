import datetime 
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib.pagesizes import letter




   
   
def create_pdf(name,email,message):
    file_name = "Contact.pdf"
    date = datetime.datetime.now()
    myemail="alajlassi624@gmail.com"
    subtitle= [f"From :{name}",f"Email :{email}",f"To :{myemail}",f'Date :{date.strftime("%d/%m/%Y, %H:%M:%S")}']
    title = "Direct Message "
    image = "assets/danke.jpeg"
    pdf = canvas.Canvas(file_name,pagesize=letter)
    pdf.setFont("Courier-Bold", 24)
    pdf.setTitle(title)
    pdf.drawCentredString(300,770,title)
    #pdf.setFillColorRGB(0,0,255)
    pdf.setFont("Courier-Bold", 20)
    subtext_y = 700
    for i in range(0,len(subtitle),1):
        subtext_x = 0
        pdf.drawString(subtext_x, subtext_y, subtitle[i])
        subtext_y = subtext_y - 30
        
       
    
    text_y = 500
    text_x = 0 
    x= [ ]
    pdf.setFont("Courier-Bold", 20)
    for i in message.split():
        pdf.drawString(text_x, text_y, i)
        text_x = len(i)*15 + text_x 
        x.append(i)
        print(i)
        if text_x > 400:
            text_y -= 30
            text_x=0
        if len(x) >= 10 :
            text_y -= 20
            print(x)
            x = [ ]
            text_x=0
        
         
    pdf.drawInlineImage(image,450,550)
    
    pdf.save() 
