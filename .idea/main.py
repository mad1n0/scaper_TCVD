from scraper import BetScraper

output_file = "dataset.csv"

print('init scraper')

scraper = BetScraper()
scraper.scrape()
scraper.data2csv(output_file)