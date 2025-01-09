import tkinter as tk
from tkinter import messagebox, simpledialog

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

    def view_contacts(self):
        return [str(contact) for contact in self.contacts]

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        return [str(contact) for contact in found_contacts]

    def update_contact(self, old_name, new_name, new_phone, new_email, new_address):
        contact = self.find_contact_by_name(old_name)
        if contact:
            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email
            contact.address = new_address
            return True
        return False

    def delete_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

class ContactBookApp:
    def __init__(self, root, contact_book):
        self.root = root
        self.contact_book = contact_book
        self.root.title("Contact Book")
        self.root.geometry("500x500")
        self.root.config(bg="#f2f2f2")
        self.create_widgets()

    def create_widgets(self):
        self.contact_listbox = tk.Listbox(self.root, width=50, height=15, bg="#e0f7fa", font=("Arial", 12))
        self.contact_listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Contact", width=20, command=self.add_contact, bg="#4caf50", fg="white", font=("Arial", 12))
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", width=20, command=self.view_contacts, bg="#2196f3", fg="white", font=("Arial", 12))
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", width=20, command=self.search_contact, bg="#ff9800", fg="white", font=("Arial", 12))
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", width=20, command=self.update_contact, bg="#ffeb3b", fg="black", font=("Arial", 12))
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", width=20, command=self.delete_contact, bg="#f44336", fg="white", font=("Arial", 12))
        self.delete_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", width=20, command=self.root.quit, bg="#9e9e9e", fg="white", font=("Arial", 12))
        self.exit_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")
        
        if name and phone and email and address:
            self.contact_book.add_contact(name, phone, email, address)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.view_contacts()
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        contacts = self.contact_book.view_contacts()
        if contacts:
            for contact in contacts:
                self.contact_listbox.insert(tk.END, contact)
        else:
            self.contact_listbox.insert(tk.END, "No contacts available.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if search_term:
            found_contacts = self.contact_book.search_contact(search_term)
            self.contact_listbox.delete(0, tk.END)
            if found_contacts:
                for contact in found_contacts:
                    self.contact_listbox.insert(tk.END, contact)
            else:
                self.contact_listbox.insert(tk.END, "No contacts found.")

    def update_contact(self):
        old_name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
        contact = self.contact_book.find_contact_by_name(old_name)
        if contact:
            new_name = simpledialog.askstring("Input", "Enter new name:", initialvalue=contact.name)
            new_phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contact.phone)
            new_email = simpledialog.askstring("Input", "Enter new email:", initialvalue=contact.email)
            new_address = simpledialog.askstring("Input", "Enter new address:", initialvalue=contact.address)
            
            if self.contact_book.update_contact(old_name, new_name, new_phone, new_email, new_address):
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.view_contacts()
            else:
                messagebox.showwarning("Error", "Contact update failed.")
        else:
            messagebox.showwarning("Error", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
        if name:
            if self.contact_book.delete_contact(name):
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.view_contacts()
            else:
                messagebox.showwarning("Error", "Contact not found.")

def main():
    contact_book = ContactBook()
    root = tk.Tk()
    app = ContactBookApp(root, contact_book)
    root.mainloop()

if __name__ == "__main__":
    main()
