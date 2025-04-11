#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 16:40:17 2025

@author: lindakovacs
"""

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        # Initialize the bank account with an account holder and an optional initial balance
        self.account_holder = account_holder
        self.balance = initial_balance

    def say_hello(self):
        # Greet the user by name
        print(f"Hello, {self.account_holder}! Welcome to your bank account.")

    def deposit(self, amount):
        # Deposit a specified amount into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True  # Indicate success
        else:
            print("Deposit amount must be positive.")
            return False  # Indicate failure

    def withdraw(self, amount):
        # Withdraw a specified amount from the account
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
                return True  # Indicate success
            else:
                print("Insufficient funds. Withdrawal denied.")
                return False  # Indicate failure
        else:
            print("Withdrawal amount must be positive.")
            return False  # Indicate failure

    def get_balance(self):
        # Return the current balance of the account
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

    def interact(self):
        # Provide a menu for the user to interact with the account
        self.say_hello()
        while True:
            print("\nWhat would you like to do?")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif choice == "3":
                self.get_balance()
            elif choice == "4":
                print("Thank you for using the bank account. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    account = BankAccount("Linda Kovacs", 100)
    account.interact()

