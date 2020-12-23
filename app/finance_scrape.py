import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pymongo
import requests
from pymongo import MongoClient

class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient("mongodb://localhost:27017")
connection = "mongodb://localhost:27017"
client = pymongo.MongoClient(connection)
db = client.FinanceDB


def scrape():
    listings = {}

    # MarketWatch
    executable_path = {"executable_path": "chromedriver"}
    MW_browser = Browser("chrome", **executable_path, headless=False)
    MW_url = "https://www.marketwatch.com/latest-news?mod=top_nav"
    MW_browser.visit(MW_url)
    MW_soup = bs(MW_browser.html, "html.parser")
    listings["MW_title"] = MW_soup.find("p", {"class":"article__summary"}).string
    


    # MW Table
    executable_path = {"executable_path": "chromedriver"}
    MW_browser = Browser("chrome", **executable_path, headless=False)
    MW_url = "https://www.marketwatch.com/investing/index/djia?mod=newsviewer_click"

    MW_table = pd.read_html(MW_url)
    MW_df = MW_table[0]
    MW_df.columns = ['loading', 'United States Financial Markets', 'Rates', 'Futures', 'US', '']
    MW_df.set_index('loading', inplace=True)
    listings["MW_table"] = MW_df.to_html()
    
  
    # Oil News 
    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    Oil_news_url = "https://oilprice.com/Latest-Energy-News/World-News/#"
    browser.visit(Oil_news_url)
    Oil_news_soup = bs(browser.html, "html.parser")
    Oil_news = Oil_news_soup.find("h3", {"class":"articleOtherNews__title"}).string
    listings["Oil_news"] = Oil_news_soup.find("h3", {"class":"articleOtherNews__title"}).string



    # Oil table
    
    OilPrice_table_url = "https://oilprice.com/oil-price-charts/#prices"
    browser.visit(OilPrice_table_url)
    OilPrice_table = pd.read_html(OilPrice_table_url)
    Oil_df = OilPrice_table[0]
    Oil_df.columns = ["", "Future & Indexes","Last", "Change","", "% Change"]
    Oil_df.set_index("Future & Indexes", inplace=True)
    listings["Oil_table"] = Oil_df.to_html()
    



    # [Reuters]
    executable_path = {'executable_path' : 'chromedriver'}
    reuters_browser = Browser("chrome", **executable_path, headless=False)
    reuters_url = "https://mobile.reuters.com/finance/markets"
    reuters_browser.visit(reuters_url)
    page = requests.get(reuters_url)
    reuters_soup = bs(page.content, 'html.parser')
    reuters_h3 = reuters_soup.find("section",class_='module top-news-module module-last').find_all("h3", {"class":"article-heading"}) 
    
 
    for reuters_headings in reuters_h3:
        print(reuters_headings.get_text())
    listings["reuters_headings"] = reuters_headings.get_text()


    return listings
    # # db.FinanceCollction.insert({listings})

















