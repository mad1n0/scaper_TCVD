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
        self.data.append(bs)



    def data2csv(self, filename):
		# Overwrite to the specified file.
		# Create it if it does not exist.
        data = self.data
        print(data)
        
        #file = open("./csv/" + 'bet2.csv', "w")
        #file.write(hola)