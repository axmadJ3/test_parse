import csv
import time
import requests
from bs4 import BeautifulSoup
import lxml


def parse(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'lxml')
    products = soup.find_all("div", class_="product-card")
    
    for product in products:
        name = product.get("data-product-name")
        name_elem = product.find("meta", itemprop="name")
        link = name_elem.findNext().get("href")
        price = product.find("span", itemprop="price").get("content")
        
        
def create_csv():
    pass

def write_csv():
    pass

def main():
    url = "https://glavsnab.net/santehnika/vanny-2.html"
    parse(url)
    
if __name__ == '__main__':
    main()
    