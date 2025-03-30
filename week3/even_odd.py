#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:22:10 2025

@author: lindakovacs
"""

# Function to check if a number is even or odd  
def check_even_or_odd():

  # Prompt the user to enter a number    
  while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    # Exit the program
    if user_input.lower() == 'q':
     print("Exiting...")
     break

    try:
      number = int(user_input)
    # Handle errors 
    except ValueError:
      print("Invalid input. Enter a number.")
      continue

    # Check if the number is even or odd  
    if number % 2 == 0:
      print(f"{number} is even number.")
    else:
      print(f"{number} is odd number.")

if __name__ == "__main__":
  check_even_or_odd()