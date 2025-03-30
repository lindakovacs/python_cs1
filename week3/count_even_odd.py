#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:11:34 2025

@author: lindakovacs
"""

# Program to determine whether 10 numbers are even or odd and count them
def count_even_odd(): 

  # Initialize counters for even and odd numbers 
  even_count = 0 
  odd_count = 0 

  # Loop to read the 10 numbers 
  for i in range(10): 
    try: 
      # Take user input for a number  
      user_input = input("Enter a number (or 'q' to quit): ")
      # Exit the program
      if user_input.lower() == 'q':
       print("Exiting...")
       break
   
      number = int(user_input)
    # Handle errors 
    except ValueError: 
      print("Invalid input. Enter an integer.") 
      continue  # Skip to the next iteration of the loop  

   # Check if the number is even or odd 
    if number % 2 == 0: 
      even_count += 1 
    else: 
      odd_count += 1 

  while True:
    display_counts = input("Do you want to display the counts? (y/n): ")
    if display_counts.lower() == 'y':
    # Display the results 
      print("Number of even numbers:", even_count)
      print("Number of odd numbers:", odd_count)
      break
    elif display_counts.lower() == 'n':
     print("Exiting without displaying counts.")
     break
    else:
     print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__": 
  count_even_odd() 