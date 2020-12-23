from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
import pymongo
from app import app
from pymongo import MongoClient
from app import finance_scrape

connection = "mongodb://localhost:27017"
client = pymongo.MongoClient(connection)

class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient("mongodb://localhost:27017")


app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)
db = client.FinanceDB



@app.route("/admin/dashboard")
def admin_dashboard():
    listings = db.listings.find_one()
    return render_template("admin/dashboard.html", listings=listings)
@app.route("/scrape")
def scraper():
    listings = db.listings
    listings_data = finance_scrape.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)

    

