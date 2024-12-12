import csv
import os
from tabulate import tabulate

def show_title():
    print("""
                    ****************************
              Welcome to the Employee Management system
                    ****************************
""")

def start_menu():
    os.system("cls")
    while True:
        try:
            show_title()
            print("""
                -----------LOGIN-------------
                
                        1. Enter
                        2. Quit
            """)
            x = int(input("Choose (1-2): "))
            if x == 1:
                check_pass()
                break
            elif x == 2:
                os._exit(0)
            else:
                print("Wrong choice! Try again.\n")
                os.system("pause")
                start_menu()
        except ValueError:
            print("Wrong input! Try again.\n")
            os.system("pause")
            start_menu()

def main_menu():
    os.system("cls")
    while True:
        try:
            print("""
                ---------------MAIN MENU ---------------------
                        1. Show All
                        2. Change Data
                        3. Find Worker
                        4. Back
            """)
            x = int(input("Choose (1-4): "))
            if x == 1:
                show_all()
                os.system("pause")
                main_menu()
                break
            elif x == 2:
                change_menu()
                break
            elif x == 3:
                os.system("cls")
                find_worker()
                break
            elif x == 4:
                return start_menu()
            else:
                print("Wrong choice! Try again.\n")
                os.system("pause")
                main_menu()
        except ValueError:
            print("Wrong input! Try again.\n")
            os.system("pause")
            main_menu()

def show_all():
    os.system("cls")
    try:
        with open('employees.csv', 'r') as f:
            data = f.readlines()
            data = [row.split(',') for row in data]
            print(tabulate(data, headers="firstrow", tablefmt='grid'))
    except FileNotFoundError:
        print("No data found!")

def change_menu():
    os.system("cls")
    while True:
        try:
            print("""
                        -------EDIT--------
                        1. New
                        2. Update
                        3. Delete
                        4. Back
            """)
            x = int(input("Choose (1-4): "))
            if x == 1:
                add_new()
                break
            elif x == 2:
                update_old()
                break
            elif x == 3:
                delete_one()
                break
            elif x == 4:
                return main_menu()
            else:
                print("Wrong choice! Try again.\n")
                os.system("pause")
                change_menu()
        except ValueError:
            print("Wrong input! Try again.\n")
            os.system("pause")
            change_menu()

def add_new():
    os.system("cls")
    cols = ['ID', 'Name', 'Surname', 'Age', 'Pay', 'Phone', 'Place']
    
    # Check if file exists and create with headers if it doesn't
    if not os.path.exists('employees.csv'):
        with open('employees.csv', 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(cols)
            
    print("\n------ADD NEW---------\n")
    id = input("ID: ")
    
    # Read existing records to check for duplicate ID
    with open("employees.csv", "r") as f:
        reader = csv.DictReader(f, fieldnames=cols)
        next(reader)  # Skip the header row
        for row in reader:
            if row["ID"] == id:
                print("ID already exists!\n")
                os.system("pause")
                change_menu()
                return

    # Add new record
    with open("employees.csv", "a", newline="") as f:
        w = csv.writer(f)
        name = input("Name: ")
        surname = input("Surname: ")
        age = input("Age: ")
        pay = input("Pay: ")
        phone = input("Phone: ")
        place = input("Place: ")
        w.writerow([id, name, surname, age, pay, phone, place])
        print("Added!")
    
    os.system("pause")
    change_menu()

def update_old():
    os.system("cls")
    show_all()
    cols = ['ID', 'Name', 'Surname', 'Age', 'Pay', 'Phone', 'Place']
    
    if not os.path.exists('employees.csv'):
        print("No data found!")
        os.system("pause")
        change_menu()
        return

    # Read all data
    all_rows = []
    with open("employees.csv", 'r') as f:
        reader = csv.DictReader(f, fieldnames=cols)
        next(reader)  # Skip header
        all_rows = list(reader)
    
    id = input("\nEnter ID: ")
    updated = False
    
    # Update the required row
    for row in all_rows:
        if row['ID'] == str(id):
            os.system("cls")
            print("\n------- UPDATE ID:", row['ID'], "-------")
            row['Name'] = input("Name: ")
            row['Surname'] = input("Surname: ")
            row['Age'] = input("Age: ")
            row['Pay'] = input("Pay: ")
            row['Phone'] = input("Phone: ")
            row['Place'] = input("Place: ")
            updated = True
            break
    
    # Write all data back
    if updated:
        with open("employees.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(cols)  # Write header
            for row in all_rows:
                writer.writerow(row.values())
        print("\nUpdated!\n")
    else:
        print("\nID not found!\n")
        
    os.system("pause")
    change_menu()

def delete_one():
    os.system("cls")
    show_all()
    cols = ['ID', 'Name', 'Surname', 'Age', 'Pay', 'Phone', 'Place']
    
    if not os.path.exists('employees.csv'):
        print("No data found!")
        os.system("pause")
        change_menu()
        return

    # Read all data
    all_rows = []
    with open("employees.csv", 'r') as f:
        reader = csv.DictReader(f, fieldnames=cols)
        next(reader)  # Skip header
        all_rows = list(reader)
    
    id = input("\nEnter ID: ")
    
    # Filter out the row to delete
    updated_rows = [row for row in all_rows if row['ID'] != str(id)]
    
    # Write back all rows except the deleted one
    if len(updated_rows) < len(all_rows):
        with open("employees.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(cols)  # Write header
            for row in updated_rows:
                writer.writerow(row.values())
        print("\nDeleted!\n")
    else:
        print("\nID not found!\n")
        
    os.system("pause")
    change_menu()
def find_worker():
    os.system("cls")
    print("\n--------SEARCH-------\n")
    if not os.path.exists('employees.csv'):
        print("No data found!")
        os.system("pause")
        main_menu()
        return

    id = input("Enter Employee ID: ")
    cols = ['ID', 'Name', 'Surname', 'Age', 'Pay', 'Phone', 'Place']
    found = False
    
    with open("employees.csv", 'r') as f:
        reader = csv.DictReader(f, fieldnames=cols)
        next(reader)  # Skip header
        for row in reader:
            if row['ID'] == id:
                print("\nEmployee Details:")
                print(tabulate(row.items(), headers=['Field', 'Value'], tablefmt='grid'))
                found = True
                break
    
    if not found:
        print("\nNo employee found with ID:", id)
    
    print("\n")
    os.system("pause")
    main_menu()
    
def check_pass():
    pwd = "12345678"
    while True:
        p = input("\nPassword: ")
        if p == pwd:
            main_menu()
        else:
            print("Wrong password!\n")
            os.system("pause")
            start_menu()

def main():
    os.system("cls")
    start_menu()

if __name__ == "__main__":
    main()