import requests
from dateutil import parser
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import time
#from scraper import BetScraper
from scraper_hltv_odds import ScraperHltvOdds
from scraper_hltv_live import ScraperHltvLive



output_file = "dataset.csv"

url_odds="https://www.hltv.org/betting/money"
url_live="https://www.hltv.org/matches"
scraper=ScraperHltvOdds(url=url_odds)
scraper.scraping_bets()
print(pd.DataFrame(scraper.data).head())

pd.DataFrame(scraper.data).to_csv(output_file,index=False)


scraper=ScraperHltvLive(url=url_live)
scraper.scraping_results()
print(pd.DataFrame(scraper.data).head())




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