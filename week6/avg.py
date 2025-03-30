#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 00:42:46 2025

@author: lindakovacs
"""

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_highest(numbers):
    return max(numbers)

def find_lowest(numbers):
    return min(numbers)

def main():
    try:
        numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
        if not numbers:
            raise ValueError("The list is empty.")

        average = calculate_average(numbers)
        highest = find_highest(numbers)
        lowest = find_lowest(numbers)

        print(f"The average is: {average:.2f}")
        print(f"The highest value is: {highest}")
        print(f"The lowest value is: {lowest}")
    except ValueError as e:
        print(f"Invalid input! {e}")

if __name__ == "__main__":
    main()

