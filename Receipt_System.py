import os
import json

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

    employees = add_employees
    print(employees)

    if manager_exists == False and employees_exist == False:
        first_time_user()
        add_employees()
    else:
        returning_user()


def does_employee_work_here(employee):
    
    file1 = open("employees.txt", "r")
    
    readfile = file1.read()
    
    if employee in readfile: 
        print("ACCESS GRANTED")
        whats_next = input("What would you like to do next?")
        if "stock" in whats_next:
            take_stock()
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

    employees = input("Enter Your Name:") 
    does_employee_work_here(employees)


def receive_payments():
    pass


def take_stock(quantity,stock,price):
    details = {"Quantity": quantity,
          "stock": stock,
          "price": price }
  
    with open('convert.txt', 'w') as convert_file:
        convert_file.write(json.dumps(details))
        pass


def store():
    check_user() 

if __name__ == "__main__":
    store()    