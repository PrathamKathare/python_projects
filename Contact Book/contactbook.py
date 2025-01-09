import os

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email} - {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found with that search term.")

    def update_contact(self, old_name, new_name, new_phone, new_email, new_address):
        contact = self.find_contact_by_name(old_name)
        if contact:
            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email
            contact.address = new_address
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Please choose an option: "))
            if choice in range(1, 7):
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_contact_ui(contact_book):
    print("\nAdd a New Contact:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book.add_contact(name, phone, email, address)

def view_contacts_ui(contact_book):
    contact_book.view_contacts()

def search_contact_ui(contact_book):
    search_term = input("\nEnter name or phone number to search: ")
    contact_book.search_contact(search_term)

def update_contact_ui(contact_book):
    old_name = input("\nEnter the name of the contact you want to update: ")
    new_name = input("Enter new name: ")
    new_phone = input("Enter new phone number: ")
    new_email = input("Enter new email: ")
    new_address = input("Enter new address: ")
    contact_book.update_contact(old_name, new_name, new_phone, new_email, new_address)

def delete_contact_ui(contact_book):
    name = input("\nEnter the name of the contact you want to delete: ")
    contact_book.delete_contact(name)

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add_contact_ui(contact_book)
        elif choice == 2:
            view_contacts_ui(contact_book)
        elif choice == 3:
            search_contact_ui(contact_book)
        elif choice == 4:
            update_contact_ui(contact_book)
        elif choice == 5:
            delete_contact_ui(contact_book)
        elif choice == 6:
            print("Exiting the Contact Book. Goodbye!")
            break

if __name__ == "__main__":
    main()
