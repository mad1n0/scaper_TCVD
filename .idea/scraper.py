import scrapy
import requests
import re
import time
from bs4 import BeautifulSoup
from dateutil import parser
import pandas as pd

class BetScraper():

    def __init__(self):
        self.url = "https://www.hltv.org/betting/money"
        self.subdomain = "betting/money.com"
        self.data = [] 
        self.response = requests.get(self.url)
        self.names = []
        self.dfs = []
        
        
    def __download_html(self, url):

        response = requests.get(url)



    def scrape(self):
        response = self.response
        url= self.url
        print ("This process could take roughly 45 minutes.\n")
        html = self.__download_html(url)
        bs = BeautifulSoup(response.text)
        all_odds = bs.findAll("table",{"class": "bookmarkerMatch"})
        print(pd.read_html(response.text))
        print(type(all_odds))
        print (all_odds)
        len_odds=len(all_odds)
        data_odds=[]
        all_names = bs.findAll("td", {"class": "odds b-list-odds"})
        u=bs.find('tr')
        print(u)
        
        for i in range(len_odds):
            names.append(all_names[i].__str__())
            data_odds.append(float((all_odds[i].__str__()).replace('<div class="odds-holder">',"").replace('</div>',"").replace(" ","")))
            
        print(data_odds)
        self.data.append(bs)



    def data2csv(self, filename):
		# Overwrite to the specified file.
		# Create it if it does not exist.
        data = self.data
        response=self.response
        #print(data)
        
        ##file = open("./csv/" + 'bet2.csv', "w")
        dfs=(pd.read_html(response.text))
        dfss = pd.concat(dfs)
        df1=dfs[1]
        dfss.to_csv('df2')