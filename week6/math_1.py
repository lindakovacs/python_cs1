#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 00:56:05 2025

@author: lindakovacs
"""

import random
import statistics
from collections import Counter

# Generate a list of 2000 random numbers
random_numbers = [random.randint(1, 100) for _ in range(2000)]

# Calculate the mode
mode = Counter(random_numbers).most_common(1)[0][0]

# Calculate the average
average = statistics.mean(random_numbers)

# Calculate the standard deviation
std_dev = statistics.stdev(random_numbers)

# Calculate the maximum value
max_value = max(random_numbers)

# Calculate the minimum value
min_value = min(random_numbers)

# Display the results
print(f"Mode: {mode}")
print(f"Average: {average:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Maximum Value: {max_value}")
print(f"Minimum Value: {min_value}")