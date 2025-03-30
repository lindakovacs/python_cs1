#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 21:05:53 2025

@author: lindakovacs
"""

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Exit")

def add_contact(contact_book):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully.")

def delete_contact(contact_book):
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def search_contact(contact_book):
    name = input("Enter the name of the contact to search: ")
    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
    else:
        print(f"Contact {name} not found.")

def display_all_contacts(contact_book):
    if contact_book:
        print("\nAll Contacts:")
        for name, info in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 20)
    else:
        print("No contacts found.")

def main():
    contact_book = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            delete_contact(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            display_all_contacts(contact_book)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

