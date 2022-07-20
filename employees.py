from re import L
import sqlite3


def first_time_user():

    print("Provide Management Details")
    man_name = input("Name\n")
    man_surname = input("Surname\n")
    man_role = input("Job Title\n")

    management = sqlite3.connect("management.db") #Added Multiple instances of the sqlite3. connect because I have to assign different databasess
    man = management.cursor()
    man.execute("""CREATE TABLE management (
        Name text, 
        Surname text,
        Management Role text)""")

    man.execute("""INSERT INTO management (Name, Surname, Management Role) VALUES (?,?,?)"""),(man_name, man_surname, man_role)
    management.commit()
    management.close()

    store = input("The name of your store: ")
    for_receipt = open("store.txt","w+")
    for_receipt.write(f"{store}")
    for_receipt.close()


def add_employees():

    emlpoyees = int(input("Number of employees: "))
    log_employees(emlpoyees)
    return emlpoyees

def log_employees(employee):

    employees = sqlite3.connect("employees.db")
    emp = employees.cursor()
    emp.execute("""CREATE TABLE employees (
        Name text, 
        Surname text,
        Job_Title text)""")       

    print("ENTER EMPLOYEE DETAILS")
    for i in range(employee):
        
        name = input(f"Employee {i+1}'s Name\n")
        surname = input(f"Employee {i+1}'s Surname\n")
        job_title = input(f"Employee {i+1}'s Job Title\n")

        emp.execute("""INSERT INTO employees 
        (Name, Surname, Job_Title)
        VALUES (?, ?, ?)"""), (name, surname, job_title)

    employees.commit()
    employees.close()     

    print("You have successfully added employees to the store databese")
    print("Please rerun the programme to start adding stock and getting your receipts")
        