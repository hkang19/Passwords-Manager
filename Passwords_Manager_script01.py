'''Passwords Manager
Project Started Date: 05/14/2022
-To save passwords and create an account list
-To search passwords by names or other keywords
-To crypto the file 
Account_Title: Name|username|passwords|email|date|comment
'''
from cryptography.fernet import Fernet
import csv

path = r"C:\Users\Betty\Desktop\Python\Password_Manager\passwords.csv"
def create_account():
    name = input("Name: ")
    username = input("Username: ")
    passwords = input("Passwords: ")
    email = input("Email: ")
    date = input("Date[MM/DD/YYYY]: ")
    comment = input("Comment: ")
    account = [name, username, passwords, email, date, comment]
    with open(path,"a",newline="") as f: 
        thewriter = csv.writer(f)
        thewriter.writerow(account)

def delete_account(): 
    row_number = int(input("Enter the row number to delete: "))
    Delete_message = "Deleted Row [" + str(row_number) + "] Successfully!"
    record = []
    with open(path,"r") as inp:
        reader = csv.reader(inp, delimiter=",")
        for row in reader:
            record+=[row] 
    record.pop(int(row_number))
    with open(path,"w",newline="") as f: 
        thewriter = csv.writer(f)
        for i in record:
                thewriter.writerow(i)
    print(Delete_message) 

def search_account():
    choice = str(input("Enter the value to search: "))
    with open(path,"r") as f: 
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if choice in row[:]: 
                print(row)
          
def view_file():
    with open(path,"r") as f: 
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            print(row)    

def deaful_setting():
    title = ["Name", "Username", "Passwords", "Email", "Date", "Comment"]
    with open(path,"w",newline="") as f: 
        thewriter = csv.writer(f)
        thewriter.writerow(title) 
    
def main():
    menu_choice = '''
    --------------------------
    Menu
    def |[Deafult]To reset to deafult setting(clear all)
    del |[delete] To delete an account
    v   |[View]   To view the entire csv_file
    c   |[Copy]   To create a copy of the csv_file
    e   |[Exit]   To exit the menu
    0   |[Create] To create an account 
    1   |[Search] To search an account by keys/keywords
    --------------------------
    '''
    error_message = "Sorry, your keys/numbers cannot be found. Please review the meanu and try agian!"
    print(menu_choice)
    choice = str(input("Enter the Menu keys/number: "))
    if choice == "def":
        deaful_setting()
    elif choice == "del":
        delete_account()
    elif choice == "v":
        view_file()
    elif choice == "0":
        create_account()
    elif choice == "1":
        search_account()
    else:
        print(error_message)
main()