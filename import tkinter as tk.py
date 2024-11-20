import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")
        
        # Create labels and entry fields for contact details
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.phone_label = tk.Label(master, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Create buttons for adding, searching, and deleting contacts
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        # Initialize a list to store contacts
        self.contacts = [] 
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        
        if not name or not phone:
            messagebox.showwarning("Error", "Please enter name and phone number")
            return
        
        new_contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(new_contact)
        self.clear_fields()
        
    def search_contact(self):
        search_term = self.name_entry.get()
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact["name"].lower():
                messagebox.showinfo("Contact Found", f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
                found = True
                break
        if not found:
            messagebox.showwarning("Not Found", "Contact not found")
        
    def delete_contact(self):
        # Implement logic to delete a contact (e.g., using a listbox to select a contact)
        pass
        
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        
# Create main window and run the application
root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()