from lib.loader import page_source_loader
from lib.reader import html_scraper
from lib.writer import data_to_csv

print("OLX Web Scraper!")
fname = input("File name: ")

input_url = input("URL: ")

page_source = page_source_loader(input_url)
data = html_scraper(page_source=page_source)

# This uploads the final data to mongodb, You
# may also write the same to a csv file by making use of 
# the data_to_csv function from the lib.writer module.
data_to_csv(fname, data) 



