import requests
from dateutil import parser
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time
#from scraper import BetScraper
from scraper_hltv_cuotas import ScraperHltvOdds

output_file = "dataset.csv"

url="https://www.hltv.org/betting/money"

scraper=ScraperHltvOdds(url=url)
scraper.scraping_bets()
print(pd.DataFrame(scraper.data).head())

pd.DataFrame(scraper.data).to_csv(output_file,index=False)


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