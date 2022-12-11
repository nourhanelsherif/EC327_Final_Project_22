from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
import math

#using chrome to open up the website
driver = webdriver.Chrome()

total_cost = []
list_needed = []
part_name =[]
# products = []
prices = []
quantity = []
website = []
qty_multiple = []

#access the website
url = "https://www.newark.com/"
def get_uml(search_term):
    template = 'https://www.newark.com/search?st={}&gs=true'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

#user's inputs
input = 'dtc143zet1g'
url = get_uml(input)
driver.get(url)
user_qty = 30

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

def OptQuant(quantity_list, price_list, qty_want):

    min = float('inf')
    pack_amt = [None]*(len(quantity_list))
    priceperpack=[None]*(len(quantity_list))
    tp_list=[None]*(len(quantity_list))

    for i in range(0, len(quantity_list)):
        pack_amt[i]=math.ceil(qty_want/(quantity_list[i]))
        #check: print(pack_amt[i])
        priceperpack[i]=(quantity_list[i])*(price_list[i])
        #check: print(priceperpack[i])

        tp_list[i]=pack_amt[i]*priceperpack[i]
    
        if tp_list[i]<min:
            min = round(tp_list[i],2)
            indmin=i
            buy_sizepack=quantity_list[i]
            buy_numpack=pack_amt[i]
            buy_totalitemcost=min

    return buy_sizepack, buy_numpack, buy_totalitemcost


count = 0
temp = soup.find_all('tr', attrs={'class': 'productRow'})

#check if the input has mutltiple different products
if temp:
    print("in if statment")
    for a in temp:
        quantity_list = []
        price_list = []

        #check if it's in stock
        in_stock=a.find('td', {'class': 'availability'}).find('p', {'class': 'enhanceInStkTxt'})
        if in_stock:
            name = a.find('a').get_text(strip = True)
            web = a.find('a')['href']
            print(web)

            # print(web)
            error_test = a.find_all('p', attrs={'class': 'errorText'})
            # print(error_test)
            qty_class = error_test[0].find_all("span")
            min_qty = qty_class[0]['data-value']
            multiple = qty_class[2]['data-value']

            if(int(min_qty) <= user_qty):
                # print(a.find("td", {"class": "listPrice enhanceQtyColumn"}))
                #getting the price and qtyfor each product
                for b in a.findAll("span", {"class": "priceBreak data-product-pricerow-products-" + str(count)}):
                    #get quantity
                    current_qty = b.find("span",{"class": "qty"}).get_text(strip = True)
                    current_qty = int(current_qty.split("+")[0])
    

                    #get quantity_price
                    qty_price = b.find("span", {"class": "qty_price_range"}).get_text(strip = True)
                    qty_price = float(qty_price.split("$")[1])

                    quantity_list.append(current_qty)
                    price_list.append(qty_price)
                
                
                
                qty, need, cost = OptQuant(quantity_list, price_list, user_qty)

                total_cost.append(cost)
                list_needed.append(need)
                quantity.append(qty)
                qty_multiple.append(multiple)
                website.append(web)
                part_name.append(name)


        
        count = count +1  

else:
    quantity_list = []
    price_list = []
    
    multqty = soup.find("div", {"class": "multqty"})
    ct = 1
    for c in multqty.findAll("span"):
        if ct == 1:
            multiple = c.find('strong').get_text(strip = True)
        else:
            min_qty = int(float(c.find('strong').get_text(strip = True)))


    if int(min_qty) <= user_qty:
        for b in soup.findAll("tr", {"class": "data-product-pricerow-main-0 pricToolCol"}):
            # print(b)

            current_qty = b.find("td",{"class": "qty"})
            current_qty = current_qty.get_text(strip = True)
            current_qty = int(current_qty.split("+")[0])
        
            #get qty price
            qty_price_class = b.find("span", {"class": "qty_price_range"})
            qty_price_class = qty_price_class.get_text(strip = True)
            qty_price = float(qty_price_class.split("$")[1])

            quantity_list.append(current_qty)
            price_list.append(qty_price)


            #get qty
            
            # print(qty)

        qty, need, cost = OptQuant(quantity_list, price_list, user_qty)

        total_cost.append(cost)
        list_needed.append(need)
        quantity.append(qty)
        qty_multiple.append(multiple)
        website.append(url)
        part_name.append(input)


#output
data = list(zip(part_name, quantity, total_cost,list_needed, website))
# print(data)