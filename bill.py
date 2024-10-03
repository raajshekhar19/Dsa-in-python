def generatebill():
    totalamount = 0
    itemdetails = []  

    while True:
        itemname = input("Enter the item name or type 'f' to end billing: ")
        if itemname.lower() == 'f':
            break
        itemquantity = float(input(f"Enter the quantity of {itemname}: "))
        itemprice = float(input(f"Enter the price per unit of {itemname}: "))
        totalamount += itemquantity * itemprice
        itemdetails.append((itemname, itemquantity, itemprice))

    print(end="\n")
    print("***********************BILL*************************************",end='\n')
    print("ITEM NAME       ITEM QUANTITY       ITEM PRICE",end='\n')
    print("****************************************************************",end='\n')
    for item in itemdetails:
        print(f"{item[0]:<15}{item[1]:<15}\t{item[2]:>12.2f}")

    print("****************************************************************",end='\n')
    print(f"TOTAL AMOUNT TO BE PAID: {totalamount:.2f} Rs",end='\n')
    print("****************************************************************",end='\n')

generatebill()
