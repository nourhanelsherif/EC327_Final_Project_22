from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome()
products = []
prices = []
quantity = []
ratings=[]
website = []
url = "https://www.newark.com/"

def get_uml(search_term):
    template = 'https://www.newark.com/search?st={}&gs=true'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

url = get_uml('pn2222a')
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

#getting the product description
name = soup.find("p", {"class": "productDecription"}).get_text(strip = True)
products.append(name)

#getting the product website
product_web = soup.find("p", {"class": "productDecription"}).parent['href']
website.append(product_web)


#getting the product price
qty_price = soup.find("span", {"class": "qty_price_range"}).get_text(strip = True)
qty_price = qty_price.split("$")[1]
print(qty_price)
prices.append(qty_price)



total_qty_price = soup.findAll("span",{"class": "qty_price_range"})
length = len(total_qty_price)
for x in range(0,length):
    qty_price = total_qty_price[x].get_text(strip = True)
    qty_price = qty_price.split("$")[1]
    print(qty_price)
    prices.append(qty_price)

total_qty = soup.findAll("span",{"class": "qty"})
length = len(total_qty)
for x in range(0, length):
    qty = total_qty[x].get_text(strip = True)
    qty = qty.split("+")[0]
    print(qty)
    quantity.append(qty)
    




