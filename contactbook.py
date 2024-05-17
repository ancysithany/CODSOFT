contacts = {}

def add_contact(name, phone_number, email, address):
    contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
    print("Contact added successfully!")

def view_contact_list():
    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone_number']}")

def search_contact(search_term):
    found = False
    for name, details in contacts.items():
        if search_term in name or search_term == details['phone_number']:
            found = True
            print(f"Name: {name}")
            print(f"Phone: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
    if not found:
        print("Contact not found.")

def update_contact(name):
    if name in contacts:
        print("Current details:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone_number']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        
        phone_number = input("Enter new phone number (leave blank to keep current): ")
        if phone_number:
            contacts[name]['phone_number'] = phone_number
        
        email = input("Enter new email (leave blank to keep current): ")
        if email:
            contacts[name]['email'] = email
        
        address = input("Enter new address (leave blank to keep current): ")
        if address:
            contacts[name]['address'] = address
        
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            update_contact(name)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()