from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index1():
    print(123)
    return "ok"

app.run(port="6000")