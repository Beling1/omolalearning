
from flask import Flask,render_template
app=Flask(__name__, template_folder='.')

@app.route("/")
def index():
    return render_template("templates/index.html")
	
@app.route("/VBA")
def vba():
    return render_template("templates/vba.html")
	
@app.route("/PYTHON")
def python():
    return render_template("templates/python.html")
	
@app.route("/CFA")
def cfa():
    return render_template("templates/cfa.html")
	
