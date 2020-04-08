import scrapy
import requests
import re
import time
from bs4 import BeautifulSoup
from dateutil import parser
import pandas as pd
import datetime


class BetScraper():

    def __init__(self):
        self.url = "https://www.hltv.org/betting/money"
        self.subdomain = "betting/money.com"
        self.data = [] 
        self.response = requests.get(self.url)
        self.names = []
        self.dfs = []
        self.merge = []
        self.dataframestomerge=[]
        self.timestamplist=[]
        
    def __download_html(self, url):
        response = requests.get(url)
    
    
    
    def scrape(self):
        response = self.response
        url= self.url
        html = self.__download_html(url)
        bs = BeautifulSoup(response.text)
        all_odds = bs.findAll("table",{"class": "bookmarkerMatch"})
        len_odds=len(all_odds)
        data_odds=[]
        all_names = bs.findAll("td", {"class": "odds b-list-odds"})
        u=bs.find('tr')
        
        for i in range(len_odds):
            names.append(all_names[i].__str__())
            data_odds.append(float((all_odds[i].__str__()).replace('<div class="odds-holder">',"").replace('</div>',"").replace(" ","")))

        self.data.append(bs)



    def data2csv(self, i):
		# Overwrite to the specified file.
		# Create it if it does not exist.
        timestamplist=self.timestamplist
        dataframestomerge=self.dataframestomerge
        data = self.data
        response=self.response
        dfs=(pd.read_html(response.text))
        dfss = pd.concat(dfs)
        timestamplist.append(datetime.datetime.now())
        dataframestomerge.append(dfss)
        dfss.to_csv('betdata'+str(i)+'.csv', index=0)


    def mergedfs(self):

        #Este método lo que hace en realidad es concatenar los dataframes usados para generar la lista de CSV's "betdata", pero no los
        #abre directamente. ¿Igual sería mejor por si se corta el proceso hacerlo escribiendo documentos cada vez?

        timestamplist=self.timestamplist
        dataframestomerge = self.dataframestomerge
        dataframestomerge=pd.concat(dataframestomerge)
        dataframestomerge.to_csv('merged_bets.csv', index=0)
        print(timestamplist)
        #for x in dfs2:
            #dfx = pd.read_csv('betdata'+str(x)+'.csv')
            #merge.append(dfx)
            #merged = pd.concat(merge)
        #merged.to_csv('merged.csv', index=0)