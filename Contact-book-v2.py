import json
print("=====Contact-Book=====")

contacts = {
            }


def load_contact():
     with open("contacts.json" , "w") as file:
        json.dump(contacts, file)
        return contacts   

def dump_contact(contacts):
     with open("contacts.json" , "w") as file:
             json.dump(contacts, file)

contacts = load_contact()
#functions here
def view_contacts():
    contacts = load_contact()
    contacts_count = len(contacts)
    if contacts_count == 0:
            print("Contact book is empty!")

    else:
        for key in contacts:
            print(f"{key}: {contacts[key]}")

def add_contact():
        update_key = input("Name: ")
        updated_number = input("Number: ")
        contacts = load_contact()
        contacts[update_key] = updated_number
        
        dump_contact(contacts)
        print("Successfully added!")

def remove_contact():
        contacts = load_contact()
        for key in contacts:
            print(f"{key}: {contacts[key]}")
        try:
            contact_name = input("which one you want to delete?: ")
            dump_contact(contacts)
            del contacts[contact_name]
            print("successfully deleted!")

        except KeyError:
            print("contact not found.")

while True:
    print("1. Veiw contacts")
    print("2. Add contact")
    print("3. Remove contact")
    print("4. Exit")
    

    choice = input("Choice: ")
    if choice == "1":
        view_contacts()

    elif choice == "2":
        add_contact()

    elif choice == "3":
            if len(contacts) == 0:
                 print("contactbook is empty")
            else:
                remove_contact()

    elif choice == "4":
        print("See you soon :)")
        break

    else:
        print("Invalid Input")