import requests
from dateutil import parser
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time
#from scraper import BetScraper
from scraper_scripts.scraper_hltv_odds import ScraperHltvOdds
from scraper_scripts.scraper_hltv_live import ScraperHltvLive

output_file = "data/dataset.csv"

url_odds="https://www.hltv.org/betting/money"
url_live="https://www.hltv.org/matches"
scraper=ScraperHltvOdds(url=url_odds)
odds_data=scraper.scraping_bets()
#print(pd.DataFrame(scraper.data).head())
timestamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

scraping_dataset=odds_data
scraping_dataset['Score']="Unknown"
scraping_dataset['Timestamp']=timestamp

scraper=ScraperHltvLive(url=url_live)
score_table=scraper.scraping_results()

if score_table==1:
    print('There is no live match and it is not going to update the dataset')
    output_file_2="prueba.csv"
    pd.DataFrame(scraping_dataset).to_csv(output_file_2,index=False)
    exit(1)
#print(pd.DataFrame(scraper.data).head())


for i in range(len(scraping_dataset)):
    bet=scraping_dataset.iloc[i,:]
    score=score_table[(score_table['match']==bet['Match']) & (score_table['team']==bet['Team'])]['score']
    time_score=score_table[(score_table['match']==bet['Match']) & (score_table['team']==bet['Team'])]['timestamp']
    scraping_dataset['Score'][i]=score
    scraping_dataset['Timestamp'][i]=time_score


output_file_2="prueba.csv"
pd.DataFrame(scraping_dataset).to_csv(output_file_2,index=False)


#timetosleep=1
#print('init scraper')
#scraper = BetScraper()
#documentnumber=0
#start = datetime.datetime.now()
#while datetime.datetime.now() <= (start + datetime.timedelta(seconds=5)):
#    scraper.scrape()
#    scraper.data2csv(documentnumber)
#    documentnumber=documentnumber+1
#    time.sleep(timetosleep)
#
#scraper.mergedfs()
#scraper.scrape_realtimescore()
#
#
#
#"https://www.hltv.org/betting/money", "https://www.hltv.org/live"
