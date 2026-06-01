import time
import json

contacts = []

running = True


def save():
    with open("contact.json", "w") as file:
        json.dump(contacts, file)


def load():
    global contacts

    try:
        with open("contact.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []


def menu():
    print("Which feature would you like to use?")
    print("1. Add contact\n2. View All\n3. Delete Contact\n4. Search Contact\n5. Edit Contact\n6. Exit")

    choice = input()

    if choice == "6":
        save()
        exit()

    elif choice == "5":
        edit()

    elif choice == "1":
        add_contact()

    elif choice == "2":
        print(f"Total contacts: {len(contacts)}")
        for contact in contacts:
            print("------------------")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print("------------------")
            time.sleep(2)

    elif choice == "3":
        delete()
        
    elif choice == "4":
        search()
    
    else:
        print("Invalid Command")
        time.sleep(1)

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")

    if not phone.isdigit():
        print("Invalid phone number")
        return


    contacts.append({"Name" : name,
                     "Phone": phone,
                     "Email": email})
    print("Added Successfully")
    save()
    time.sleep(2)
    

def delete():
    for index, contact in enumerate(contacts, start=1):
        print(f"""
--------------------------------
{index}. Name: {contact["Name"]}
   Phone: {contact["Phone"]}
   Email: {contact["Email"]}
---------------------------------""")
    try:
        choice = int(input("Which would you like to delete? "))
    except ValueError:
        print("Enter Valid Value")
        return

    if 1 <= choice <= len(contacts):
        contacts.pop(choice - 1)
        print("Deleted Successfully")
        save()
        time.sleep(1.5)
    else:
        print("Invalid contact number")


def search():
    user = input("Enter the name you want to search: ")
    found = False

    for contact in contacts:
        if user.lower() == contact["Name"].lower():
            print(f"""
------------------------------
Name: {contact["Name"]}
Phone: {contact["Phone"]}
Email: {contact["Email"]}
-------------------------------""")
            found = True
            time.sleep(1.5)

    if not found:
        print("Name not found!")
        time.sleep(1.5)
        return
        

def edit():
    user = input("Enter name you want to edit: ")
    found = False
    for contact in contacts:
        if user.lower() == contact["Name"].lower():
            found = True
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")

            if not new_phone.isdigit():
                print("Invalid phone number")
                return

            contact["Name"] = new_name
            contact["Phone"] = new_phone
            contact["Email"] = new_email
            
            print("Edited Successfully")
            save()

    if not found:
        print("Name Not Found")
        time.sleep(1)
        return            

def main():
    load()
    while running:
        menu()

main()