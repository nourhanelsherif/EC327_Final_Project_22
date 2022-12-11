import math

#this is to optimize quantity and price for each search result

#user's input
qty_want = 30

#pass this from scrape
quantity_list=[
    1, 10, 25, 50, 100
]

#pass this from scrape
price_list=[
    0.35, 0.261, 0.223, 0.185, 0.147
]

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

#test case
s, n, t = OptQuant(quantity_list, price_list, 30)
print(s)
print(n)
print(t)

