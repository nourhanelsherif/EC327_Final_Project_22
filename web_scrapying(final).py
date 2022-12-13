from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd #export excel
import math
import tkinter as tk #GUI

#find the minimum price
def findMinPrice(total_cost):
   cost =  min(total_cost)
   i = total_cost.index(cost)
   return i


#web scraping function that will iterate through the whole website and find the specific variables 
def webScraping(input, user_qty):

    #using chrome to open up the website
    driver = webdriver.Chrome()

    total_cost = []
    part_name =[]
    # products = []
    prices = []
    quantity = []
    website = []
    qty_multiple = []
    data = None

    #access the website
    url = "https://www.newark.com/"

    def get_uml(search_term):
        template = 'https://www.newark.com/search?st={}&gs=true'
        search_term = search_term.replace(' ', '+')
        return template.format(search_term)

    #user's inputs
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
            quantity_list = []
            price_list = []

            #check if it's in stock
            in_stock=a.find('td', {'class': 'availability'}).find('p', {'class': 'enhanceInStkTxt'})
            if in_stock:
                name = a.find('a').get_text(strip = True)
                web = a.find('a')['href']

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
                    
                    
                    cost, qty = OptQuant(quantity_list, price_list, user_qty)

                    total_cost.append(cost)
                    quantity.append(qty)
                    website.append(web)
                    part_name.append(name)


            
            count = count +1  

    else:
        quantity_list = []
        price_list = []

        multqty = soup.find("div", {"class": "multqty"})
        if multqty != None:
            ct = 1
            for c in multqty.findAll("span"):
                if ct == 1:
                    multiple = c.find('strong').get_text(strip = True)
                    ct = ct+1
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

                cost, qty = OptQuant(quantity_list, price_list, user_qty)

                total_cost.append(cost)
                quantity.append(qty)
                qty_multiple.append(multiple)
                website.append(url)
                part_name.append(input)

        else:
            errorMessage(input)

    ##retunr the cheapest function here
    i = findMinPrice(total_cost)
    name = part_name[i]
    quan = quantity[i]
    cost = total_cost[i]
    web = website[i]


    #output
    check_data = list(zip(part_name, quantity, total_cost, website))
    data = list((name,quan,cost,web))

    if data==[]:
        errorMessage(input)
    else:
        return data

#if not able to find the part entered
def errorMessage(input):
    window2 = tk.Tk()
    window2.title("error message")
    window2.geometry("300x100")
    l = tk.Label(window2, text = "Not able to find item" + input)
    l.pack()

#finding the cheapeast way to buy products
qty_want = 15

#pass this from scrape
quantity_list=[
    1, 10, 20, 50, 100
]

#pass this from scrape
ppu_list=[
    0.35, 0.261, 0.223, 0.185, 0.147
]

#fn starts here
def OptQuant(quantity_list, ppu_list, qty_want):
    #find the quantity choices closest to the quantity wanted and their indices
    min1 = float('inf')
    min2 = float('inf')

    diff_list = []

    for quantity in quantity_list:
        diff = qty_want - quantity
        diff_list.append(diff)

        if (diff < min1 and diff>=0):
            qmin1=quantity
            index1=diff_list.index(diff)
        
    index2=index1+1
    q2=quantity_list[index2]

    #print(diff_list)
    #print(qmin1)
    #print(q2)
    #print(index1)
    #print(index2)
    #works

    tp1=round(qty_want*ppu_list[index1],2)
    tp2=round(q2*ppu_list[index2],2)

    #print(tp1)
    #print(tp2)

    if tp1<=tp2:
        tpmin=tp1
        qbuy=qty_want

    if tp1>tp2:
        tpmin=tp2
        qbuy=q2

    #print(tpmin)
    #print(qbuy)

    return tpmin, qbuy


# clean up all the user's enter
def cleanUp(window):
    for widget in window.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, 'end')

#producing the parts
def generating(window):
    check = 0
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            if(widget['text'] == "Part"):
                check = 1 #check is part
            elif(widget['text'] == "Qty"):
                check = 2 # check is qty
            elif(widget['text'] == "budget"):
                check = 3
            
        elif isinstance(widget, tk.Entry):
            if(check == 1):
                part = widget.get()
                inputList.append(part)
            elif(check == 2):
                qty = int(widget.get())
                user_qtyList.append(qty)
            elif(check == 3):
                budget = widget.get()

    for i in range(0, len(user_qtyList)):
        return_data = webScraping(inputList[i], user_qtyList[i])
        output_data.append(return_data)

    #output the data to excel file
    df = pd.DataFrame(output_data, columns = ['part', 'quantity', 'total cost', 'website'])
    df.to_excel('output.xlsx')
    # print(df)
    
    #check if it's within the budget
    w3 = tk.Tk()
    w3.geometry("400x300")
    w3.title("Ouput")
    cost = df.loc[: , "total cost"]
    genText = tk.Label(w3, text = "output file is generated in Output.txt")
    genText.pack()
    total = sum(cost)
    #enoguh budget
    if(total <= float(budget)):
        outputText = tk.Label(w3, text = "total cost is "+ str(total))
        outputText.pack()
    else:#not enough budget
        limitedBudgettext = tk.Label(w3, text = "Not enough budget")
        outputText = tk.Label(w3, text = "total cost is "+ str(total))
        outputText.pack()
        limitedBudgettext.pack()





def partEnter():
    window = tk.Tk()
    num = num_entry.get()
    if(int(float(num))<=5):
        xValue = 400
        yValue = int(float(num)) * 130 + 20 * (5-int(float(num)))
    else:
        xValue = 800
        yValue = 700

    
    size = str(xValue) + "x" + str(yValue)
    window.geometry(size)
    window.title("Auto BOM")
    window.resizable(False, False)

    for i in range(0, int(float(num))):
        if(i<5):
            #if only 5 parts needed, it gonna print one column
            partText = tk.Label(window, text="Part")
            partText.place(x=300, y = 10 + 110 * (i))
            part_entry = tk.Entry(window, width = 15)
            part_entry.place(x=240, y = 30+ 110*(i))
            part = part_entry.get()

            qtyText = tk.Label(window, text="Qty")
            qtyText.place(x=300, y = 60+110*(i))
            qty_entry = tk.Entry(window, width = 10)
            qty_entry.place(x=260, y = 80+110*(i))

        
        elif(i<10):
            #if more than 5 parts needed, it will print two columns
            partText = tk.Label(window, text="Part")
            partText.place(x=600, y = 20 + 110 * (i-5))
            part_entry = tk.Entry(window, width = 15)
            part_entry.place(x=540, y = 30+ 110*(i-5))
            part = part_entry.get()

            qtyText = tk.Label(window, text="Qty")
            qtyText.place(x=600, y = 60+110*(i-5))
            qty_entry = tk.Entry(window, width = 10)
            qty_entry.place(x=560, y = 80+110*(i-5))


        budgetText = tk.Label(window, text="budget")
        budgetText.place(x= 20, y = 40)
        budgetInput = tk.Entry(window, width = 10)
        budgetInput.place(x=10, y = 60)

        #generate and clear button will be printed at the end of window
        gen_button = tk.Button(window, text = 'Generate', width = 10, command = lambda: generating(window))
        gen_button.place(x=20, y = yValue - 50)

        clear_button = tk.Button(window, text = 'Clear', width = 10, command = lambda: cleanUp(window))
        clear_button.place(x=220, y = yValue - 50)


    window.mainloop()


inputList = []
user_qtyList = []
output_data = []
budget = 0

#create the window to urge user to enter num of parts they need
w = tk.Tk()
w.geometry("400x150")
w.title("Please enter a number")
w.resizable(False, False)
numText = tk.Label(text="How many parts do you want")
numText.pack()
maxiText = tk.Label(text="maximum number is 10")
maxiText.pack()
num_entry = tk.Entry(width = 15)
num_entry.pack()

#pop a window when generate button is pressed
generate_button = tk.Button(text = 'Generate', width = 10, command = lambda: partEnter())
generate_button.pack()

w.mainloop()

