from flask import Flask, render_template, request, redirect   
from database import loaddb



app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html", jobs=loaddb(), Company="Parayil"  )

JOBS= [
  {"id":1,"title":"Data Analyst","location":"Bengaluru, India","salary":"100K"},
  {"id":2,"title":"Data Scientist","location":"Delhi, India","salary":"200k"}
   
]

if __name__=="__main__":
  print("i am inside you")
  app.run(host='0.0.0.0', debug=True)