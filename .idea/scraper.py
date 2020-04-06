import scrapy

import urllib3
import re
import time
from bs4 import BeautifulSoup
from dateutil import parser


class BetScraper():

    def __init__(self):
        self.url = "https://www.hltv.org/betting/money"
        self.subdomain = "betting/money.com"
        self.data = [] 
        self.response = urllib3.PoolManager.request()
        
        
        
    def __download_html(self,url):
        http =  urllib3.PoolManager()
        response = http.request('GET', url)



    def scrape(self):
        response = self.response
        url= self.url
        print ("This process could take roughly 45 minutes.\n")
        html = self.__download_html(self, url)
        bs = BeautifulSoup(response.data)
        self.data.append(bs)


    def data2csv(self, filename):
		# Overwrite to the specified file.
		# Create it if it does not exist.
        file = open("../csv/" + filename, "w+")

		# Dump all the data with CSV format
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                file.write(self.data[i][j] + ";")
            file.write("\n")