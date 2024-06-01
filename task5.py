import tkinter as tk
from tkinter import messagebox
import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and phone number are required.")
        return

    contacts = load_contacts()
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()

def view_contacts():
    contacts = load_contacts()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_term = entry_search.get()
    contacts = load_contacts()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a contact to update.")
        return

    index = selected[0]
    contacts = load_contacts()
    contact = contacts[index]

    contact['name'] = entry_name.get()
    contact['phone'] = entry_phone.get()
    contact['email'] = entry_email.get()
    contact['address'] = entry_address.get()

    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact updated successfully!")
    view_contacts()

def delete_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a contact to delete.")
        return

    index = selected[0]
    contacts = load_contacts()
    contacts.pop(index)
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact deleted successfully!")
    view_contacts()

def on_select(event):
    selected = listbox_contacts.curselection()
    if not selected:
        return

    index = selected[0]
    contacts = load_contacts()
    contact = contacts[index]

    entry_name.delete(0, tk.END)
    entry_name.insert(0, contact['name'])
    entry_phone.delete(0, tk.END)
    entry_phone.insert(0, contact['phone'])
    entry_email.delete(0, tk.END)
    entry_email.insert(0, contact['email'])
    entry_address.delete(0, tk.END)
    entry_address.insert(0, contact['address'])

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Name:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white", width=15).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Update Contact", command=update_contact, bg="#2196F3", fg="white", width=15).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="#f44336", fg="white", width=15).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="View Contacts", command=view_contacts, bg="#FFC107", fg="black", width=15).grid(row=5, column=1, padx=10, pady=10)

tk.Label(root, text="Search:", bg="#f0f0f0").grid(row=6, column=0, padx=10, pady=5, sticky='e')
entry_search = tk.Entry(root, width=30)
entry_search.grid(row=6, column=1, padx=10, pady=5)
tk.Button(root, text="Search", command=search_contact, bg="#9C27B0", fg="white", width=15).grid(row=7, column=1, padx=10, pady=10)

listbox_contacts = tk.Listbox(root, width=50, height=10)
listbox_contacts.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
listbox_contacts.bind('<<ListboxSelect>>', on_select)

view_contacts()

root.mainloop()
