contacts_dictionary = {}

def add_contact():
    contact_name = input("What is the name of the contact you would like to add?: ")
    contact_number = input("What is the phone number of the contact you would like to add?: ")
    print(f"The contact {contact_name} with the number {contact_number} has been added.")
    contacts_dictionary[contact_name] = contact_number

    
def remove_contact():
    contact_name = input("What is the name of the contact you would like to remove?: ")
    if contact_name in contacts_dictionary:
        del contacts_dictionary[contact_name]
        print("The contact", contact_name, "has been removed")
    else:
        print("The contact", contact_name, "is not in the dictionary")

def view_contacts():
    print(contacts_dictionary)


    

def main_menu():
        while True: 
            choose = input("Would you like to add a contact, remove a contact, view contacts, or exit? (add,remove,view,exit): ").lower() 
            if "add" in choose:
                add_contact()   
            elif "remove" in choose:
                remove_contact()
            
            elif "view" in choose:
                view_contacts()
            elif "exit" in choose:
                break
            else:
                print("Please a valid option")

main_menu()