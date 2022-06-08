import os
import json
from re import S


def first_time_user():

    print("Provide Management Details")
    manager = input("Name Surname Job Title\n")
    management = open("management.txt","w+")
    management.write(f"{manager}")
    management.close()

    store = input("The name of your store: ")
    for_receipt = open("store.txt","w+")
    for_receipt.write(f"{store}")
    for_receipt.close()


def add_employees():

    emlpoyees = int(input("Number of employees: "))
    log_employees(emlpoyees)
    return emlpoyees

    
def check_user():

    manager_exists = os.path.exists('management.txt')
    employees_exist = os.path.exists("employees.txt")
    
    if manager_exists == False and employees_exist == False:
        first_time_user()
        add_employees()
    
    elif employees_exist == False:
        add_employees()

    else:
        returning_user()


def does_employee_work_here(employee):
    
    file1 = open("employees.txt", "r")
    file2 = open("management.txt", "r")
    
    readfile = file1.read()
    read_nextfile = file2.read()
    
    if employee in readfile or employee in read_nextfile: 
        print("ACCESS GRANTED")
        whats_next = input("What would you like to do next?\n")
        if "stock" in whats_next:
            stock_market()
        elif "payment" in whats_next:
            receive_payments()
        else:
            print("System does not understand command.\nUse keywords 'payment' or 'stock'.")
    else: 
        with open('store.txt') as store:
            shop = store.readline()
            print("ACCESS DENIED")
            print(f"You are not in {shop}'s list of employees")
            print("Shutting down....") 
    
    file1.close() 

    
def log_employees(employee):

    employees = open("employees.txt","w+")
    for i in range(employee):
        name = input(f"Enter employee {i+1}'s Full Name and position\n")
        employees.write(f"{name}\n")
        each_employee = open(f"{i+1}. {name}.txt","w+")

    print("You have successfully configured the system to work with your store")
    print("Please rerun the programme to start adding stock and getting your receipts")
    

def returning_user():

    employees = input("Enter Your Name: ") 
    does_employee_work_here(employees)


def receive_payments():
    pass


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

    for i in range(stock_number):

        stock = input(f"Name/Lable of item {i+1}\n")
        quantity = input(f"How many {stock}'s are you adding?\n")
        price = input(f"Price of {stock}\nR ")

        details = {"Quantity": quantity,
            "stock": stock,
            "price": price }        

        with open('stock.txt', 'w+') as stock:
            stock.write(json.dumps(details))

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


def store():
    check_user() 

if __name__ == "__main__":
    store()    