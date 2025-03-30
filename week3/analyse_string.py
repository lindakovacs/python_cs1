#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:02:37 2025

@author: lindakovacs
"""

# Program to analyze a favorite phrase from a song
# Reads a string from the user, calculates the number of characters, 
# and determines if the character count is even or odd.
def analyze_string():

  # Prompt the user to enter their favorite phrase
  favorite_song = input("Enter your favorite phrase from a song: ")
  # Calculate the number of characters in the phrase (including spaces and punctuation)
  char_count = len(favorite_song)

  # Determine if the count is even or odd
  if char_count % 2 == 0:
    result = "even"
  else:
    result = "odd"

  # Display results
  print(f"\nYour favorite phrase from a song: {favorite_song}")
  print(f"\nNumber of characters: {char_count}")
  print(f"\nThe character count is {result}.")

if __name__ == "__main__":
  analyze_string()