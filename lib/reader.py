from bs4 import BeautifulSoup

def html_scraper(page_source):

    soup = BeautifulSoup(page_source, 'html.parser')
    apt_listings_ul = soup.find("div", attrs={"data-testid": "listing-grid"})
    listings = apt_listings_ul.find_all("div", attrs={"data-cy": "l-card"})

    data = []
    for listing in listings:
        ad_link = listing.find("a")["href"]
        if ad_link.find('https://') == -1:
            ad_link = 'https://www.olx.ro' + ad_link
        try:
            ad_title = listing.find("h6", attrs={"class":"css-16v5mdi er34gjf0"}).string
            if ad_title.find('Floresti') != -1:
                continue
            if ad_title.find('Florești') != -1:
                continue
            if ad_title.find('Baciu') != -1:
                continue
            if ad_title.find('Apahida') != -1:
                continue
            if ad_title.find('Iris') != -1:
                continue
        except:
            ad_title = "NOTFOUND!"
        try:
            ad_price = listing.find("p", attrs={"data-testid":"ad-price"}).text
        except:
            ad_price = "NOTFOUND!"
        try:
            ad_size = listing.find("span", attrs={"class":"css-643j0o"}).text
        except:
            ad_size = "NOTFOUND!"
        data.append([ad_title, ad_price, ad_size, ad_link])
    
    return data
