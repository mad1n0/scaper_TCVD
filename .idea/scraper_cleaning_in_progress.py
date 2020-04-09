import requests
from bs4 import BeautifulSoup as bs
from dateutil import parser
import pandas as pd
import numpy as np
import datetime


class BetScraper():

    def __init__(self,url):
        #Inicializamos todos los valores necesarios
        self.url, self.response,self.body=url, requests.get(url,headers={'Content-Type': 'text/html'}),bs(self.response.text)
        self.data, self.names, self.dfs, self.merge, self.dataframes_to_merge, self.timestamp_list = [],[],[],[],[], []
        #self.liveresponse =  requests.get(self.liveurl)

        
    def scraping_realtime(self):
        
        
        
    def scraping_bets(self):
        
        #EXTRAER TODAS LAS CUOTAS
        data_raw=pd.read_html(response.text)
        self.data.append(data_raw)
        
        #EXTRAER LAS DIFERENTES CASAS DE APUESTAS
        u=body.find_all('tr')
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

        
        
        
        
        
        
    #NOTA: ¿LOS COMENTARIOS EN ESPAÑOL O EN INGLÉS?
    def data2csv(self, i):
		# Overwrite to the specified file.
		# Create it if it does not exist.
        timestamp_list=self.timestamp_list
        dataframes_to_merge=self.dataframes_to_merge
        data = self.data
        response=self.response
        dfs=(pd.read_html(response.text))
        dfss = pd.concat(dfs)
        timestamplist.append(datetime.datetime.now())
        dataframes_to_merge.append(dfss)
        dfss.to_csv('betdata'+str(i)+'.csv', index=0)


    def mergedfs(self):

        #Este método lo que hace en realidad es concatenar los dataframes usados para generar la lista de CSV's "betdata", pero no los
        #abre directamente. ¿Igual sería mejor por si se corta el proceso hacerlo escribiendo documentos cada vez?

        timestamplist=self.timestamplist
        dataframes_to_merge = self.dataframes_to_merge
        dataframes_to_merge=pd.concat(dataframes_to_merge)
        dataframestomerge.to_csv('merged_bets.csv', index=0)
        print(timestamplist)
        #for x in dfs2:
            #dfx = pd.read_csv('betdata'+str(x)+'.csv')
            #merge.append(dfx){"team": team, "odds": odds, "match": match, "provider":provider, "timestamp": timestamp}
            #merged = pd.concat(merge)
        #merged.to_csv('merged.csv', index=0)
        
        


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
url="https://www.hltv.org/betting/money"
response = requests.get(url, headers={'Content-Type': 'text/html'})
body=bs(response.text)
all_odds=body.find_all('div',class_="odds-holder")
len_odds=len(all_odds)
data_odds=[]
for i in range(len_odds):
    data_odds.append(float((all_odds[i].__str__()).replace('<div class="odds-holder">',"").replace('</div>',"").replace(" ","")))


prueba=body.find_all('table',class_="bookmakerMatch")
dfs=pd.read_html(response.text)
dfss = pd.concat(dfs)
dfss=dfss[1:].iloc[:,0:len(dfss.columns)-1].replace(" ","")
num_regs=len(dfss)


u=body.find_all('tr')
uy=u[0].find_all('td')

providers=[]
probe=[node['class'] for node in u[0].find_all() if ((node.has_attr('class')) & (len(node)==1))]

num_matches=int(len(dfss)/2)

for provider in probe:
     if len(provider)>1:
        if len(provider)==3:
            provider_name=provider[1]+"-"+provider[2]
        elif len(provider)==2:
            provider_name=provider[1]
        provider_name=provider_name.replace("b-list-","")
        providers.append(provider_name)


team0=np.arange(0,num_regs-1,step=2)
team1=np.arange(1,num_regs,step=2)
matches=[]

data_all=pd.DataFrame()
mathes_per_row=[]
for i in range(num_matches):
    matches.append(dfss[0].iloc[team0[i]].__str__() +"-vs-"+dfss[0].iloc[team1[i]].__str__()+"yearmonthday")
    mathes_per_row.append(dfss[0].iloc[team0[i]].__str__() +"-vs-"+dfss[0].iloc[team1[i]].__str__()+"yearmonthday")
    mathes_per_row.append(dfss[0].iloc[team0[i]].__str__() +"-vs-"+dfss[0].iloc[team1[i]].__str__()+"yearmonthday")


    
data_all['Match']=[]
data_all['Provider']=[]
data_all['Bet']=[]
data_all['Team']=[]

bets_elements=[]
provider_elements=[]
team_elements=[]

match_elements=[]

j=0
for row in dfss.values:
    i=0
    bets=row[1:]
    team=row[0]
    for bet in bets:
        bets_elements.append(bet)
        provider_elements.append(providers[i])
        match_elements.append(mathes_per_row[j])
        team_elements.append(team)
        i=i+1
    j=j+1

data_all['Provider']=provider_elements
data_all['Bet']=bets_elements
data_all['Team']=team_elements

data_all['Match']=match_elements
data_all['Timestamp']="fecha"





data_all.to_csv('prueba_data_all.csv',index=False)



    def scrape_realtimescore(self):
        liveresponse = self.liveresponse
        liveurl=self.liveurl
        liveresponse = requests.get(liveurl)
        print(liveresponse)
        
        #livedf = pd.read_html(liveresponse.text)
        

    #NOTA: ENTIENDO QUE ESTOS DOS METODOS SE QUITARAN YA QUE SOLAMENTE LLAMAN A UN COMANDO
        
    #def __download_html(self, url):    
    #    response = requests.get(url)
    #
    #def __download_html2(self, liveurl):
    #    liveresponse = requests.get(liveurl)
    #    print(liveresponse)