import math

#this is to optimize quantity and price for each search result possible, simplifies data that is scraped

#user's input
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

#test case
p, q = OptQuant(quantity_list, ppu_list, 15)
print(p)
print(q)
