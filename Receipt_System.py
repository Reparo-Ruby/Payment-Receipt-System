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

    does_employee_work_here()


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
        if "payment" in whats_next:
            receive_payments()    
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
    print("Please rerun the programme to start getting your receipts")
    

def returning_user():

    employees = input("Enter Your Name: ") 
    does_employee_work_here(employees)


def receive_payments():
    pass


def take_stock():
   
    what_item = input("what item would you like to see?\n")
    with open('stock', 'w+') as stock:
        details = stock.read()
    if what_item in details:
        print(f"You have {details['Quantity']} {what_item} left. ")
    else:
        print(f"{what_item} is not in the stores stock list.")    


def add_stock(employee,file):

    details = {"Quantity": quantity,
          "stock": stock,
          "price": price }

    with open('stock', 'w+') as stock:
        stock.write(json.dumps(details))
    pass

    stock = input("Name/Lable of the item\n")
    quantity = input(f"How many {stock} are you adding?\n")

    if employee in file: ##this is for the manager we will only check if the manager exists only she is allowed to change prices
        price = input(f"Price of {stock}\nR ")


def stock_market():

    add_or_take = input("Do you want to do Stock Taking or Add Stock?")
    if add_or_take.lower() == "stock taking": 
        take_stock()
    elif add_or_take.lower() == "add stock":
        add_stock()    
    
    file1 = open("convert.txt", "r")
    print(file1.read())


def store():
    check_user() 

if __name__ == "__main__":
    store()    