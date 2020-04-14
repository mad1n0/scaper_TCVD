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
        data_raw=self.body
        self.data_raw.append(df_raw)

        #### ID_MATCHES ####
        tables=data_raw.find_all(lambda tag: tag.name == 'table' and tag.get('class') == ['table'])
        id_matches=np.array([tab.get('data-livescore-match') for tab in tables])
        id_matches=id_matches[id_matches!=None]

        num_regs=2*len(id_matches)
        team0=np.arange(0,num_regs-1,step=2)
        team1=np.arange(1,num_regs,step=2)
        
        if num_regs>2:
            matches_id=np.zero(num_regs)
            for i in range(len(id_matches)):
                    matches_id[team0[i]]=id_matches[i]
                    matches_id[team1[i]]=id_matches[i]
        elif num_regs==2:
            matches_id=np.array([id_matches,id_matches])
        
        matches_id=matches_id.astype('int')



        #### SCORES ####
        scores_maps=np.array(data_raw.find_all('span'))
        
        p=[("data-livescore-maps-won-for" in x.__str__()) for x in scores_maps]
        scores_maps=scores_maps[p]
        score_team=[]
        
        for score in scores_maps:
            score_team.append([score['data-livescore-team'],score.get_text()])
        
        #### SCORES DATAFRAME ####
        score_table=pd.DataFrame()
        score_table['team']=np.array(score_team)[:,0]
        score_table['score']=np.array(score_team)[:,1]
        score_table['matches']=matches_id
        self.data=score_table
        return score_table
