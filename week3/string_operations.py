#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:26:06 2025

@author: lindakovacs
"""

# Program to concatenate and interlock two strings
def string_operations():

  # Read two strings from the user
  string1 = input("Enter the first string: ")
  string2 = input("Enter the second string: ")

  # Concatenate strings
  concatenated_string = string1 + string2

  # Interlock strings
  interlocked_string = ""
  for i in range(min(len(string1), len(string2))):
    interlocked_string += string1[i] + string2[i]
  interlocked_string += string1[i:] + string2[i:]  # Add remaining characters

  # Display the results
  print(f"\nConcatenated String: {concatenated_string}")
  print(f"\nInterlocked String: {interlocked_string}")

if __name__ == "__main__":
  string_operations()