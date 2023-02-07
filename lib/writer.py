import csv

def data_to_csv(filename, data):
    with open(f'scraped_data/{filename}.csv', 'w', newline='', encoding="utf-8") as file: 
        writer = csv.writer(file)
        headers = ['Ad Title', 'Price', 'Ad Size', 'Ad Link',]
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)
