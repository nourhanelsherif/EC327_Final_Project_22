from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome()
products = []
prices = []
ratings=[]
url = "https://www.newark.com/"

def get_uml(search_term):
    template = 'https://www.newark.com/search?st={}&gs=true'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

url = get_uml('pn2222a')
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
name = soup.find("p", {"class": "productDecription"}).get_text(strip = True)
products.append(name)
print(products)

qty_price = soup.find("span", {"class": "qty_price_range"}).get_text(strip = True)
qty_price = qty_price.split("$")[1]
print(qty_price)
prices.append(qty_price)




# things doesn't work
qty_price2 = soup.findNext({"class": "qty_price_range"}).get_text(strip = True)
qty_price2 = qty_price2.split("$")[1]
print(qty_price2)
prices.append(qty_price2)

# test = soup.findal("tr", class_ = "productRow  hasAltProd ")
# print(test)
# for a in soup.find_all("tr", {"class": "productRow  hasAltProd "}):
#     print(a)
#     p = a.find("span", {"class": "qty_price_range"}).get_text(strip = True)
#     print(p)

# print(products)



