
from flask import Flask,render_template
app=Flask(__name__, template_folder='.')

@app.route("/")
def home():
    return render_template("template/index.html")
	
@app.route("/VBA")
def vba():
    return render_template("vba.html")
	
@app.route("/PYTHON")
def python():
    return render_template("python.html")
	
@app.route("/CFA")
def cfa():
    return render_template("cfa.html")
	
