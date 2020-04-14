
import requests
from dateutil import parser
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time
from getMatchId import getidlist

class ScraperHltvOdds():

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
        try:
            self.url, self.response=url, requests.get(url,headers=headers,timeout=5)
        except requests.exceptions.RequestException:
            pass
        self.body=bs(self.response.text)
        self.data_raw, self.names, self.dfs, self.merge, self.dataframes_to_merge, self.timestamp_list,self.data,self.providers = [],[],[],[],[],[],[],[]
        #self.liveresponse =  requests.get(self.liveurl)
        
    def scraping_bets(self):
        #Extract all the main tables with the odds and the team information, clean it and save it on the scraper object 
        data_raw=pd.read_html(self.response.text)
        df_raw = pd.concat(data_raw)
        df_raw=df_raw[1:].iloc[:,0:len(df_raw.columns)-1].replace(" ","")
        self.data_raw.append(df_raw)
        num_regs=len(df_raw)
        num_matches=int(len(df_raw)/2)
        
        #Extract all the odds providers and save the info into the scraper
        u=self.body.find_all('tr')
        providers=[]
        providers_regs=[node['class'] for node in u[0].find_all() if ((node.has_attr('class')) & (len(node)==1))]
        for provider in providers_regs:
            if len(provider)>1:
                if len(provider)==3:
                    provider_name=provider[1]+"-"+provider[2]
                elif len(provider)==2:
                    provider_name=provider[1]
                provider_name=provider_name.replace("b-list-","")
                providers.append(provider_name)
        self.providers=providers

        #Extract all the teams and matches which happen
        team0=np.arange(0,num_regs-1,step=2)
        team1=np.arange(1,num_regs,step=2)
        mathes_per_row=[]
        data_all=pd.DataFrame()
        
        idlist = getidlist()

        
        for i in range(num_matches):
            mathes_per_row.append(df_raw[0].iloc[team0[i]].__str__() +"-vs-"+df_raw[0].iloc[team1[i]].__str__()+"-yearmonthday")
            mathes_per_row.append(df_raw[0].iloc[team0[i]].__str__() +"-vs-"+df_raw[0].iloc[team1[i]].__str__()+"-yearmonthday")

        #Build the final dataframe
        data_all['Match']=[]
        data_all['Provider']=[]
        data_all['Bet']=[]
        data_all['Team']=[]
        
        bets_elements=[]
        provider_elements=[]
        team_elements=[]
        match_elements=[]        
        

        j=0
        for row in df_raw.values:
            i=0
            bets=row[1:]
            team=row[0]
            for bet in bets:
                bets_elements.append(bet)
                provider_elements.append(providers[i])
                match_elements.append(idlist[j])
                team_elements.append(team)
                i=i+1
            j=j+1

        data_all['Provider']=provider_elements
        data_all['Bet']=bets_elements
        data_all['Team']=team_elements
        data_all['Match']=match_elements
        data_all['Timestamp']="fecha"
        #data_all=pd.DataFrame(data_all)
        self.data=data_all
        return data_all
