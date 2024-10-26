import time
import csv

import requests
from bs4 import BeautifulSoup
import lxml

from model import Product


def parse(url: str, max_item: int):
    create_csv()
    
    page = 1
    count_items = 0
    while max_item > count_items:
        response = requests.get(url=f"{url}?p={page}")
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        products = soup.find_all("div", class_="product-card")
        
        list_products = []
        for product in products:
            if count_items >= max_item:
                break
            
            count_items += 1
            name = product.get("data-product-name")
            name_elem = product.find("meta", itemprop="name")
            link = name_elem.findNext().get("href")
            try:
                price = product.find("span", itemprop="price").get("content")
            except Exception:
                price = 'По запросу'
                
            list_products.append(Product(name=name, price=price, link=link))
        
        write_csv(list_products)
        page += 1
        
        
def create_csv():
    with open('glavsnab.csv', "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'name',
            'price',
            'link'
        ])


def write_csv(product_list: list[Product]):
    with open('glavsnab.csv', "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for product in product_list:
            writer.writerow([
                product.name,
                product.price,
                product.link
                
            ])


def main():
    url = "https://glavsnab.net/santehnika/vanny-2.html"
    parse(url, max_item = 680)
    
    
if __name__ == '__main__':
    main()
    