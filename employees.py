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

def log_employees(employee):

    employees = open("employees.txt","w+")
    for i in range(employee):
        name = input(f"Enter employee {i+1}'s Full Name and position\n")
        employees.write(f"{name}\n")
        each_employee = open(f"{i+1}. {name}.txt","w+")

    print("You have successfully configured the system to work with your store")
    print("Please rerun the programme to start adding stock and getting your receipts")
        