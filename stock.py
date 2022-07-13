import os
import json

def take_stock():
   
    what_item = input("what item would you like to see?\n")
    with open('stock.txt', 'w+') as stock:
        details = stock.read()
    if what_item in details:
        print(f"You have {details['Quantity']} {what_item} left. ")
    else:
        print(f"{what_item} is not in the stores stock list.")   

def add_stock():

    stock_number = int(input("How many items do you wanna add as stock?\n"))

    # stock = []

    for i in range(stock_number):

        product = input(f"Name/Lable of item {i+1}\n")
        quantity = input(f"How many {product}'s are you adding?\n")
        price = input(f"Price of {product}\nR ")

        details = {"Quantity": quantity,
            "product": product,
            "price": price } 

        # stock.append(details)           

        with open('stock.txt', 'a') as stock:
            stock.write(json.dumps(details) + "\n")

    print("STOCK ADDED")        
   

def stock_market():

    add_or_take = input("Do you want to do Stock Taking or Add Stock?\n")
    if add_or_take.lower() == "stock taking":
        if os.path.exists('store.txt') == True:
            take_stock()
        else:
            print("There is no stock in the store.")    
    elif add_or_take.lower() == "add stock":
        add_stock()    
    
    # file1 = open("store.txt", "r")
    # print(file1.read())

