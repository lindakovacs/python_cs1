#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 22:36:14 2025

@author: lindakovacs
"""

import os

def display_menu():
    print("\nMenu of Operations:")
    print("1. Find Average")
    print("2. Find Maximum")
    print("3. Find Minimum")
    print("4. Find Sum")
    print("5. Find Standard Deviation")
    print("6. Find Variance")
    print("7. Exit")

def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [float(line.strip()) for line in file]
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except ValueError:
        print("Error: The file contains non-numeric data.")
        return None

def write_result(file_path, operation, result):
    try:
        with open(file_path, 'a') as file:  # Open in append mode
            file.write(f"{operation}: {result}\n")
        print(f"Result written to '{file_path}' successfully.")
    except IOError:
        print(f"Error: Could not write to file '{file_path}'.")

def find_average(data):
    return sum(data) / len(data)

def find_maximum(data):
    return max(data)

def find_minimum(data):
    return min(data)

def find_sum(data):
    return sum(data)

def find_standard_deviation(data):
    mean = find_average(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5

def find_variance(data):
    mean = find_average(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def create_data_file(file_path):
    numbers_added = False
    try:
        with open(file_path, 'w') as file:
            print("Enter numbers to add to the data file (type 'done' to finish):")
            while True:
                user_input = input("Enter numbers separated by spaces: ")
                if user_input.lower() == 'done':
                    break
                try:
                    numbers = [float(num) for num in user_input.split()]
                    for number in numbers:
                        file.write(f"{number}\n")
                    numbers_added = True
                except ValueError:
                    print("Invalid input. Enter numeric values separated by spaces.")
        if not numbers_added:
            os.remove(file_path)
            print("No numbers were added. The data file was not created.")
        else:
            print(f"Data file '{file_path}' created successfully.")
    except IOError:
        print(f"Error: Could not create file '{file_path}'.")

def main():
    input_file = 'data.txt'
    output_file = 'result.txt'

    # Check if the data file exists, if not, create it and prompt the user to add numbers
    if not os.path.exists(input_file):
        print(f"The file '{input_file}' does not exist.")
        create_data_file(input_file)

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting the program. Goodbye!")
            break

        data = read_data(input_file)
        if data is None:
            continue

        if choice == '1':
            result = find_average(data)
            operation = "Average"
        elif choice == '2':
            result = find_maximum(data)
            operation = "Maximum"
        elif choice == '3':
            result = find_minimum(data)
            operation = "Minimum"
        elif choice == '4':
            result = find_sum(data)
            operation = "Sum"
        elif choice == '5':
            result = find_standard_deviation(data)
            operation = "Standard Deviation"
        elif choice == '6':
            result = find_variance(data)
            operation = "Variance"
        else:
            print("Invalid choice. Enter a number between 1 and 7.")
            continue

        print(f"{operation}: {result}")
        write_result(output_file, operation, result)

if __name__ == "__main__":
    main()