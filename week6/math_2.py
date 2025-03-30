#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 01:01:06 2025

@author: lindakovacs
"""

import random
import statistics
from collections import Counter

# Generate a list of 2000 random numbers
random_numbers = [random.randint(1, 100) for _ in range(2000)]

# Function to calculate the mode
def calculate_mode(numbers):
    count = Counter(numbers)
    mode = count.most_common(1)[0][0]
    return mode

# Function to calculate the average
def calculate_average(numbers):
    return statistics.mean(numbers)

# Function to calculate the standard deviation
def calculate_std_dev(numbers):
    return statistics.stdev(numbers)

# Function to calculate the maximum value
def calculate_max(numbers):
    return max(numbers)

# Function to calculate the minimum value
def calculate_min(numbers):
    return min(numbers)

# Split the list into 6 sublists
sublists = [random_numbers[i::6] for i in range(6)]

# Calculate and display the results for each sublist
for i, sublist in enumerate(sublists, start=1):
    mode = calculate_mode(sublist)
    average = calculate_average(sublist)
    std_dev = calculate_std_dev(sublist)
    max_value = calculate_max(sublist)
    min_value = calculate_min(sublist)

    print(f"Sublist {i}:")
    print(f"  Mode: {mode}")
    print(f"  Average: {average:.2f}")
    print(f"  Standard Deviation: {std_dev:.2f}")
    print(f"  Maximum Value: {max_value}")
    print(f"  Minimum Value: {min_value}")
    print()