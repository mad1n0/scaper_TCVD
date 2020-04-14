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
#INIT of static variables

#How many times not adding info when there is no match going on
noliving_max=100
nolivingsteps=0

#The time between calls is defined taking account the robots.txt advice of one call per second. In order to follow the instruction we used 2 seconds of wait in order to follow it.
timetosleep=2

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
    
        scraping_dataset['Score']="Unknown"
        scraping_dataset['Living']="Unknown"
        timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        scraping_dataset['Timestamp']=timestamp
    
        scraping_dataset['Living']='NoLiving'
        
        if path.exists(orig_file):
            dataset_orig=pd.read_csv(orig_file)
        else:
            dataset_orig=scraping_dataset
            pd.DataFrame(dataset_orig).to_csv(orig_file,index=False)
        
        merged_dataset=gen_merged_dataset(merged_file,dataset_orig,scraping_dataset)
        pd.DataFrame(merged_dataset).to_csv(merged_file,index=False)
        continue
    
    
    #LIVING MATCH behaviour
   
    if path.exists(orig_file):
        dataset_orig=pd.read_csv(orig_file)
    else:
        scraper=ScraperHltvOdds(url=url_odds)
        odds_data=scraper.scraping_bets()
        scraping_dataset=odds_data
    
        scraping_dataset['Score']="Unknown"
        scraping_dataset['Living']="Unknown"
        timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        scraping_dataset['Timestamp']=timestamp
    
        scraping_dataset['Living']='NoLiving'

        dataset_orig=scraping_dataset
        pd.DataFrame(dataset_orig).to_csv(orig_file,index=False)
        
    
    #GENERATE ODDS dataset and init the full scraping dataset
    scraper=ScraperHltvOdds(url=url_odds)
    odds_data=scraper.scraping_bets()
    scraping_dataset=odds_data
    
    scraping_dataset['Score']="Unknown"
    scraping_dataset['Living']="Unknown"
    timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    scraping_dataset['Timestamp']=timestamp

    #ADD SCORE INFO to the scraping dataset
    #SE PUEDE HACER MEJOR Y QUE BUSQUE LOS REGISTROS UTILES Y NO PASAR POR TODOS
    for i in range(len(scraping_dataset)):
        bet=scraping_dataset.iloc[i,:]
        reg_bet=(score_table['match']==bet['Match']) & (score_table['team']==bet['Team'])
        if any(reg_bet):
            score=score_table[reg_bet]['score']
            #time_score=score_table[reg_bet]['timestamp']
            scraping_dataset['Score'][i]=score
            scraping_dataset['Living'][i]='Living'
    
    #MERGE previous scraping data to new
    dataset_orig=pd.read_csv(orig_file)
    merged_dataset=gen_merged_dataset(merged_file,dataset_orig,scraping_dataset)
    pd.DataFrame(merged_dataset).to_csv(merged_file,index=False)

    nolivingsteps=0
    time.sleep(timetosleep)
