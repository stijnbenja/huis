import re
import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
import json

gewenste_postcodes = [3011,3012,3013,3014,3015,3016,3021,3031,3032,3033,3035,3037,3038,3039,3061,3062,3071]
max_bedrag = 2100

url = "https://www.huurwoningen.nl/in/rotterdam/?price=0-2250&living_size=75&bedrooms=3"

def haal_op():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all("li", attrs={"class": "search-list__item search-list__item--listing"})
    
    listings = []

    base_url = "https://www.huurwoningen.nl"

    for item in results:
        
        location = item.find("div",attrs={"class":"listing-search-item__sub-title'"}).text.strip()
        
        info_dict = {
        'title':item.find("a",attrs={"class":"listing-search-item__link listing-search-item__link--title"}).text.strip(),
        'location':location,
        'prijs':int(item.find("div",attrs={"class":"listing-search-item__price"}).text.strip()[2:-10].replace(".",'')),
        'postcode': int(location[:4]),
        'url': base_url + item.find("a",attrs={"class":"listing-search-item__link listing-search-item__link--title"})['href'],
        'image_url':item.find("img",attrs={"class":"picture__image"})['src']
        }
        listings.append(info_dict)
        
    gewenste_items = [x for x in listings if x['postcode'] in gewenste_postcodes]
    gewenste_items = [x for x in gewenste_items if x['prijs'] <= max_bedrag]
    
    return gewenste_items