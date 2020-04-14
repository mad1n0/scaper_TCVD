import requests
from bs4 import BeautifulSoup
from dateutil import parser
import pandas as pd
import datetime
from scraper_scripts.getteamID import get_df
import requests
from dateutil import parser
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time


class BetScraper():

    def __init__(self):
        self.url = "https://www.hltv.org/betting/money"
        self.liveurl = "https://www.hltv.org/live"

        self.data = [] 
        self.response = requests.get(self.url)
        self.names = []
        self.dfs = []
        self.merge = []
        self.dataframestomerge=[]
        self.timestamplist=[]
        self.liveresponse =  requests.get(self.liveurl)
        
    def __download_html(self, url):
        response = requests.get(url)
    
    def __download_html2(self, liveurl):
        liveresponse = requests.get(liveurl)
        print(liveresponse)
    
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


    def scrape_realtimescore(self):
        liveresponse = self.liveresponse
        liveurl=self.liveurl
        liveresponse = requests.get(liveurl)
        print(liveresponse)
        
        #livedf = pd.read_html(liveresponse.text)

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
            #merge.append(dfx){"team": team, "odds": odds, "match": match, "provider":provider, "timestamp": timestamp}
            #merged = pd.concat(merge)
        #merged.to_csv('merged.csv', index=0)
        
    def score_filler(scraping_dataset,living):
        
        scraping_dataset['Score']="Unknown"
        timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        scraping_dataset['Timestamp']=timestamp
        teams_id=get_df()
        
        #ADD SCORE INFO to the scraping dataset
        #SE PUEDE HACER MEJOR Y QUE BUSQUE LOS REGISTROS UTILES Y NO PASAR POR TODOS
        for i in range(len(scraping_dataset)):
            bet=scraping_dataset.iloc[i,:]
            teams_id[teams_id==bet['Team']].iloc[:,0]
            reg_bet=(score_table['match']==bet['Match']) & (score_table['team']==bet['Team'])
            if any(reg_bet):
                score=score_table[reg_bet]['score']
                #time_score=score_table[reg_bet]['timestamp']
                scraping_dataset['Score'][i]=score
                scraping_dataset['Living'][i]=living
    
    
    def gen_merged_dataset(self,merged_filename,data_orig,data_new):
        data_orig=pd.read_csv(merged_filename)
        merged_dataset=pd.concat([data_orig,data_new])
        return merged_dataset

    def tablesBO():    
        url = "https://www.hltv.org/matches"
        response = requests.get(url).content
        soup = bs(response)
        b = soup.find('div', attrs= {'class' : "live-matches"})
        c = b.find_all('div', attrs= {'class' : "live-match"})
        
        tablesBO3=[]
        tablesBO1=[]
        tablesBO5=[]
        for element in c:
            print(element.find('table'))
            print(element.find('td', attrs = {'class' : "bestof"}).get_text())
            if(element.find('td', attrs = {'class' : "bestof"}).get_text() == 'Best of 3'):
                tablesBO3.append(element)
            if(element.find('td', attrs = {'class' : "bestof"}).get_text() == 'Best of 5'):
                tablesBO5.append(element)
            if(element.find('td', attrs = {'class' : "bestof"}).get_text() == 'Best of 1'):
                tablesBO1.append(element)

    return tablesBO3, tablesBO5, tablesBO1
