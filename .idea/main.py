from scraper import BetScraper
import datetime
import time
output_file = "dataset.csv"
timetosleep=1
print('init scraper')
scraper = BetScraper()
documentnumber=0
start = datetime.datetime.now()
while datetime.datetime.now() <= (start + datetime.timedelta(seconds=5)):
    scraper.scrape()
    scraper.data2csv(documentnumber)
    documentnumber=documentnumber+1
    time.sleep(timetosleep)

scraper.mergedfs()