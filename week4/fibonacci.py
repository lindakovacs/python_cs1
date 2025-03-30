#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:55:05 2025

@author: lindakovacs
"""

# Program to print Fibonacci sequence up to a specified number entered by the user.
def fibonacci_sequence():

    while True:
        try:
            # Take user input for a number
            user_input = input("Enter a number to generate the Fibonacci sequence up to (or 'q' to quit): ")
            # Exit the program
            if user_input.lower() == 'q':
                print("Exiting...")
                return  # Exit the function if the user enters 'q'

            number = int(user_input)
            if number < 0:
                print("Number must be a non-negative integer.")
                continue  # Go back to the beginning of the loop

            break  # Exit the loop ONLY if input is valid and non-negative

        except ValueError:
            print("Invalid input. Enter an integer.")
            continue  # Skip to the next iteration of the loop

    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    print("Fibonacci sequence up to", number, ":")

    while a <= number:
        print(a, end=" ")
        a, b = b, a + b  # Update values for next iteration

    print()  # Print a newline at the end


if __name__ == "__main__":
    fibonacci_sequence()