import scrapy
import requests
import re
import time
from bs4 import BeautifulSoup
from dateutil import parser


class BetScraper():

    def __init__(self):
        self.url = "https://www.hltv.org/betting/money"
        self.subdomain = "betting/money.com"
        self.data = [] 
        self.response = requests.get(self.url)
        
        
        
    def __download_html(self, url):

        response = requests.get(url)



    def scrape(self):
        response = self.response
        url= self.url
        print ("This process could take roughly 45 minutes.\n")
        html = self.__download_html(url)
        bs = BeautifulSoup(response.text)
        all_odds = bs.findAll("div",{"class": "odds-holder"}, limit = 60)
        print(type(all_odds))
        print (all_odds)
        len_odds=len(all_odds)
        data_odds=[]
        for i in range(len_odds):
            data_odds.append(float((all_odds[i].__str__()).replace('<div class="odds-holder">',"").replace('</div>',"").replace(" ","")))
            
        print(data_odds)
        self.data.append(bs)



    def data2csv(self, filename):
		# Overwrite to the specified file.
		# Create it if it does not exist.
        data = self.data
        #print(data)
        
        #file = open("./csv/" + 'bet2.csv', "w")
        #file.write(hola)