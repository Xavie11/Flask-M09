from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/ep0")
def ep0():
    return "<html><body><h1>Aquest és el meu primer endpoint</h1></body></html>"
@app.route("/ep1")

def ep1():
    return render_template("index.html")