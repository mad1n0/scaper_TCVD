from scraper import BetScraper

output_file = "dataset.csv"

scraper = BetScraper()
scraper.scrape()
scraper.data2csv(output_file)