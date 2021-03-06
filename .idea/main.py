import requests
from dateutil import parser
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time
from scraper_scripts.scraper import BetScraper
from scraper_scripts.scraper_hltv_odds import ScraperHltvOdds
from scraper_scripts.scraper_hltv_live import ScraperHltvLive
from os import path
from scraper_scripts.getteamID import get_df

#INIT of static variables

#How many times not adding info when there is no match going on
noliving_max=100
nolivingsteps=0

#The time between calls is defined taking account the robots.txt advice of one call per second. In order to follow the instruction we used 30 seconds of wait in order to follow it.
timetosleep=30

#Filename for source and output
orig_file = "data/dataset_orig.csv"
merged_file="data/dataset.csv"

#URLs where do the scraping
url_odds="https://www.hltv.org/betting/money"
url_live="https://www.hltv.org/matches"

while 1==1:
    #SCRAPING the living matches score
    scraper=ScraperHltvLive(url=url_live)
    score_table=scraper.scraping_results()

    scraper=ScraperHltvOdds(url=url_odds)
    odds_data=scraper.scraping_bets()
    scraping_dataset=odds_data

    
    #NO LIVING MATCH behaviour
    if ((not (isinstance(score_table,pd.DataFrame))) and (nolivingsteps<noliving_max)):
        print('There is no live match and it is not going to update the dataset')
        nolivingsteps=nolivingsteps+1
        time.sleep(timetosleep)
        continue
    elif ((not (isinstance(score_table,pd.DataFrame))) and (nolivingsteps==noliving_max)):
        nolivingsteps=0
        
        scraper=ScraperHltvOdds(url=url_odds)
        odds_data=scraper.scraping_bets()
        scraping_dataset=odds_data
    
      
        timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        scraping_dataset['Timestamp']=timestamp
    
        scraping_dataset['Living']='NoLiving'
        
        if path.exists(merged_file):
            dataset_orig=pd.read_csv(merged_file)
        else:
            dataset_orig=scraping_dataset
            pd.DataFrame(dataset_orig).to_csv(merged_file,index=False)
        
        merged_dataset=BetScraper().gen_merged_dataset(merged_file,dataset_orig,scraping_dataset)
        pd.DataFrame(merged_dataset).to_csv(merged_file,index=False)
        continue
    
    
    #LIVING MATCH behaviour
   
    if path.exists(merged_file):
        dataset_orig=pd.read_csv(merged_file)
    else:
        scraper=ScraperHltvOdds(url=url_odds)
        odds_data=scraper.scraping_bets()
        scraping_dataset=odds_data
    
        #scraping_dataset['Score']="Unknown"

        timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        scraping_dataset['Timestamp']=timestamp
    
        scraping_dataset['Living']='NoLiving'

        dataset_orig=scraping_dataset
        pd.DataFrame(dataset_orig).to_csv(orig_file,index=False)
        
    
    #GENERATE ODDS dataset and init the full scraping dataset
    scraper=ScraperHltvOdds(url=url_odds)
    odds_data=scraper.scraping_bets()
    scraping_dataset=odds_data
    
    timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    scraping_dataset['Timestamp']=timestamp
    scraping_dataset['Score']="Unknown"
    scraping_dataset['Living']="NoLiving"

    #ADD SCORE INFO to the scraping dataset
    #SE PUEDE HACER MEJOR Y QUE BUSQUE LOS REGISTROS UTILES Y NO PASAR POR TODOS
    for i in range(len(scraping_dataset)):
        bet=scraping_dataset.iloc[i,:]
        teams_id=get_df()
        team=teams_id[teams_id.iloc[:,0]==bet['Team']].iloc[:,1]
        if len(team)==0:
            continue
        reg_bet=(score_table['match']==int(bet['Match'])) & (score_table['team']==team.values[0])
        if any(reg_bet):
            score=score_table[reg_bet]['score']
            scraping_dataset['Score'][i]=score.values[0]
            scraping_dataset['Living'][i]='Living'
            
    #MERGE previous scraping data to new
    dataset_orig=pd.read_csv(orig_file)
    merged_dataset=BetScraper().gen_merged_dataset(merged_file,dataset_orig,scraping_dataset)
    merged_dataset=merged_dataset[merged_dataset['Living']=='Living']
    pd.DataFrame(merged_dataset).to_csv(merged_file,index=False)
    nolivingsteps=0
    time.sleep(timetosleep)
