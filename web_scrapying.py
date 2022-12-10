from selenium import webdriver
from bs4 import BeautifulSoup
import pandas

driver = webdriver.Chrome()

part_name =[]
# products = []
prices = []
quantity = []
website = []
minimum_quantity = []
qty_multiple = []
url = "https://www.newark.com/"

def get_uml(search_term):
    template = 'https://www.newark.com/search?st={}&gs=true'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

input = 'dtc143zet1g'
url = get_uml(input)
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')


count = 0
temp = soup.find_all('tr', attrs={'class': 'productRow'})

#check if the input has mutltiple different products
if temp:
    # print("in if statment")
    for a in temp:

        #check if it's in stock
        in_stock=a.find('td', {'class': 'availability'}).find('p', {'class': 'enhanceInStkTxt'})
        if in_stock:
            name = a.find('a').get_text(strip = True)
            web = a.find('a')['href']
            # print(web)

            # print(web)
            error_test = a.find_all('p', attrs={'class': 'errorText'})
            # print(error_test)
            qty_class = error_test[0].find_all("span")
            min_qty = qty_class[0]['data-value']
            multiple = qty_class[2]['data-value']

            # print(a.find("td", {"class": "listPrice enhanceQtyColumn"}))
            #getting the price and qtyfor each product
            test = 0
            for b in a.findAll("span", {"class": "priceBreak data-product-pricerow-products-" + str(count)}):
                qty_price = b.find("span", {"class": "qty_price_range"}).get_text(strip = True)
                qty_price = qty_price.split("$")[1]
                # print(qty_price)
                qty = b.find("span",{"class": "qty"}).get_text(strip = True)
                qty = qty.split("+")[0]
                prices.append(qty_price)
                quantity.append(qty)

                part_name.append(name)
                minimum_quantity.append(min_qty)
                qty_multiple.append(multiple)
                website.append(web)
        
        count = count +1  

else:
    print("in else statment")
    
    multqty = soup.find("div", {"class": "multqty"})
    ct = 1
    for c in multqty.findAll("span"):
        if ct == 1:
            multiple = c.find('strong').get_text(strip = True)
        else:
            min_qty = c.find('strong').get_text(strip = True)

    for b in soup.findAll("tr", {"class": "data-product-pricerow-main-0 pricToolCol"}):
        # print(b)

        #get qty price
        qty_price = b.find("span", {"class": "qty_price_range"})
        qty_price = qty_price.get_text(strip = True)
        qty_price = qty_price.split("$")[1]
        prices.append(qty_price)

        #get prices for each qty
        qty = b.find("td",{"class": "qty"})
        qty = qty.get_text(strip = True)
        qty = qty.split("+")[0]
        quantity.append(qty)
        # print(qty)


        minimum_quantity.append(min_qty)
        qty_multiple.append(multiple)
        website.append(url)
        part_name.append(input)



#create excel file to store the output
data = list(zip(part_name, prices, quantity, minimum_quantity, qty_multiple, website))
# print(data)

d = pandas.DataFrame(data, columns=["part_name", "prices", "quantity", "minimum_quantity", "qty_multiple", "website"])
d.to_excel(input+ ".xlsx")


    


