import requests
from dateutil import parser
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time

class ScraperHltvLive():

    def __init__(self,url):
        #Initializing all the variables which define the scraper
        headers = {
            "Accept": "text/html",
            "Accept-Language": "es-ES,en;q=0.8",
            "Cache-Control": "no-cache",
            "dnt": "1",
            "Pragma": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            'Content-Type': 'text/html'
            }
        self.url, self.response=url, requests.get(url,headers=headers)
        self.body=bs(self.response.text)
        self.data_raw, self.names, self.dfs, self.merge, self.dataframes_to_merge, self.timestamp_list,self.data,self.providers = [],[],[],[],[],[],[],[]
        #self.liveresponse =  requests.get(self.liveurl)

    def scraping_results(self):
        #Extract all live matches scores
        data_raw=self.body
        self.data_raw.append(df_raw)
        
        #The data is separated by every match
        live_matches_raw=data_raw.find_all('div',{'class':"live-match"})


        for match in live_matches_raw:
            #Score of the losing team
            losing_score=match.find('span',{'class':"trailing"}).get_text()
                        
            #Score of the winning team
            winning_score=match.find('span',{'class':"leading"}).get_text()
            
            #Score for a tied match
            tie_score=match.find('span',{'class':"tie"}).get_text()
            
            ###HAY QUE VER COMO DISTINGUIR EL NOMBRE DEL EQUIPO QUE ESTÁ GANANDO CON EL NOMBRE DEL EQUIPO QUE ESTÁ PERDIENDO Y SU SCORE
            
            team_names=match.find_all('span',{'class':"team-name"})
            
            match_name.append(team_names[0].get_text()+'-vs-'+team_names[1].get_text()+'-yearmmdd')
            
        self.matches=matches_name
        self.data=data_all
