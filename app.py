from flask import Flask, render_template, request, redirect   



app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")


if __name__=="__main__":
  print("i am inside you")
  app.run(host='0.0.0.0', debug=True)