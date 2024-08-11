import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")

        self.contacts = {}

        # Create UI elements
        self.name_label = tk.Label(root, text="Name:", font=("Arial", 12))
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(root, text="Phone Number:", font=("Arial", 12))
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)

        self.phone_entry = tk.Entry(root, font=("Arial", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = tk.Label(root, text="Email:", font=("Arial", 12))
        self.email_label.grid(row=2, column=0, padx=10, pady=10)

        self.email_entry = tk.Entry(root, font=("Arial", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = tk.Label(root, text="Address:", font=("Arial", 12))
        self.address_label.grid(row=3, column=0, padx=10, pady=10)

        self.address_entry = tk.Entry(root, font=("Arial", 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, font=("Arial", 12))
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts, font=("Arial", 12))
        self.view_button.grid(row=4, column=1, padx=10, pady=10)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact, font=("Arial", 12))
        self.search_button.grid(row=5, column=0, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, font=("Arial", 12))
        self.update_button.grid(row=5, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, font=("Arial", 12))
        self.delete_button.grid(row=6, column=0, padx=10, pady=10)

        self.contact_listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=10)
        self.contact_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
            self.clear_entries()
            self.view_contacts()
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name} - {details['phone']}")

    def search_contact(self):
        query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if query:
            results = [f"{name} - {details['phone']}" for name, details in self.contacts.items() if query in name or query in details['phone']]
            if results:
                self.contact_listbox.delete(0, tk.END)
                for result in results:
                    self.contact_listbox.insert(tk.END, result)
            else:
                messagebox.showinfo("No Results", "No contacts found.")

    def update_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            name = self.contact_listbox.get(selected).split(" - ")[0]
            if name in self.contacts:
                phone = simpledialog.askstring("Update Phone", "Enter new phone number:", initialvalue=self.contacts[name]["phone"])
                email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=self.contacts[name]["email"])
                address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=self.contacts[name]["address"])

                self.contacts[name] = {"phone": phone, "email": email, "address": address}
                messagebox.showinfo("Success", f"Contact {name} updated successfully!")
                self.view_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")

    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            name = self.contact_listbox.get(selected).split(" - ")[0]
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {name}?"):
                del self.contacts[name]
                messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
                self.view_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
