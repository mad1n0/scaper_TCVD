# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 03:09:48 2020

@author: Marc
"""


import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
import time
import re
class ScraperHltvGetTeamIds():

    def __init__(self,url):
        #Initializing all the variables which define the scraper
        self.url, self.response=url, requests.get(url,headers={'Content-Type': 'text/html'})
        self.body=BeautifulSoup(self.response.text)
        self.data_raw, self.names, self.dfs, self.merge, self.dataframes_to_merge, self.timestamp_list,self.data,self.providers = [],[],[],[],[],[],[],[]
        #self.liveresponse =  requests.get(self.liveurl)
        
    def scraping_teams(self):
        #Extract all the main tables with the odds and the team information, clean it and save it on the scraper object 
        url = self.url
        data_raw=pd.read_html(self.response.text)
        bs4 = self.response.text
        self.body = BeautifulSoup(bs4)
        all_names = self.body.findAll('td')
        tag_a =  all_names[0]
        
        #for id, tg in enumerate(all_names):
            #tag_a = tg[id].find('a')
            #for st in tag_a:
                #print(st.text)
        
        print(bs4)