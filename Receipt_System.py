import os
from employees import add_employees, first_time_user
from payments import receive_payments
from stock import stock_market

    
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


def receipt_system(employee):
    
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
    

def returning_user():

    employees = input("Enter Your Name: ") 
    receipt_system(employees)

def store():
    check_user() 

if __name__ == "__main__":
    store()    