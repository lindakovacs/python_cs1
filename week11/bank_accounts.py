#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:55:31 2025

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
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw a specified amount from the account
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        # Return the current balance of the account
        print(f"Current balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0, interest_rate=0.02):
        # Initialize the savings account with an interest rate
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def say_hello(self):
        # Greet the user and specify the account type
        print(f"Hello, {self.account_holder}! Welcome to your Savings Account.")

    def add_interest(self):
        # Add interest to the balance
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} added. New balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0, overdraft_limit=100):
        # Initialize the checking account with an overdraft limit
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def say_hello(self):
        # Greet the user and specify the account type
        print(f"Hello, {self.account_holder}! Welcome to your Checking Account.")

    def withdraw(self, amount):
        # Override the withdraw method to allow overdraft
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Withdrawal denied. Exceeds overdraft limit.")
        else:
            print("Withdrawal amount must be positive.")


def interact_with_account(account, savings_account, checking_account):
    # Provide a menu for the user to interact with the account
    account.say_hello()
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        if isinstance(account, SavingsAccount):
            print("4. Add Interest")
        print("5. Switch Account")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.get_balance()
        elif choice == "4" and isinstance(account, SavingsAccount):
            account.add_interest()
        elif choice == "5":
            # Switch account
            if isinstance(account, SavingsAccount):
                print("Switching to Checking Account...")
                interact_with_account(checking_account, savings_account, checking_account)
            else:
                print("Switching to Savings Account...")
                interact_with_account(savings_account, savings_account, checking_account)
            break
        elif choice == "6":
            print("Thank you for using the bank account. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def main():
    print("Welcome to the Bank Account System!")
    # Create both accounts
    savings_account = SavingsAccount("Linda Kovacs", 1000, 0.05)
    checking_account = CheckingAccount("Linda Kovacs", 500, 200)

    print("Choose an account type to start:")
    print("1. Savings Account")
    print("2. Checking Account")
    account_choice = input("Enter your choice (1 or 2): ")

    if account_choice == "1":
        interact_with_account(savings_account, savings_account, checking_account)
    elif account_choice == "2":
        interact_with_account(checking_account, savings_account, checking_account)
    else:
        print("Invalid choice. Exiting the program.")


if __name__ == "__main__":
    main()
