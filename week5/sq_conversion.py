#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:42:12 2025

@author: lindakovacs
"""

def sqft_to_sqm(sqft):
    return sqft * 0.092903

def sqm_to_sqft(sqm):
    return sqm / 0.092903

def main():
    print("Square Feet and Square Meters Conversion Program")
    print("1. Convert Square Feet to Square Meters")
    print("2. Convert Square Meters to Square Feet")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        try:
            sqft = float(input("Enter area in Square Feet: "))
            sqm = sqft_to_sqm(sqft)
            print(f"{sqft} SqFt is equal to {sqm:.2f} SqMt")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    elif choice == '2':
        try:
            sqm = float(input("Enter area in Square Meters: "))
            sqft = sqm_to_sqft(sqm)
            print(f"{sqm} SqMt is equal to {sqft:.2f} SqFt")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    else:
        print("Invalid choice. Enter 1 or 2.")

if __name__ == "__main__":
    main()

