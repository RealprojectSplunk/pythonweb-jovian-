from flask import Flask

app=Flask(__name__)
@app.route("/")
def hello():
    return "<p>Hello, World!</p>"


if 1==1:
  print("i am inside you")
  app.run(host='0.0.0.0',debug=True)