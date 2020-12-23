from app import app
from flask import render_template



@app.route("/")
def index():
    return render_template("general/index.html")

@app.route("/general/portfolio")
def portfolio():
    return render_template("general/portfoli.html")

@app.route("/general/resume")
def resume():
    return render_template("general/resume.html")

@app.route("/general/GeneralML")
def main_ML():
    return render_template("general/GeneralML.html")
    
@app.route("/general/supervised")
def suprvised():
    return render_template("general/supervised.html")

@app.route("/general/unsuprvised")
def unsuprvised():
    return render_template("general/unsupervised.html")

@app.route("/general/unsuprvised")
def reinforced():
    return render_template("general/reinforced.html")

@app.route("/general/HowScrape")
def HowScrape():
    return render_template("general/HowScrape.html")





