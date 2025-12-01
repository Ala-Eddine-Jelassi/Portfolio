from  pymongo import MongoClient
from Backend.generatePdf import create_pdf
url = ""
client = MongoClient(url)
db = client["Portfolio_WebApp"]
collection = db["contacts"]

def insert_data(name,email,message):
    data = {"Name":name,"email":email,"message":message}
    create_pdf(name,email,message)
    response = collection.insert_one(data)
    print("inserted------------------")
    print(response)
