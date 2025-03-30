#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 22:05:18 2025

@author: lindakovacs
"""

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

def write_result(file_path, result):
    try:
        with open(file_path, 'w') as file:
            file.write(str(result))
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

def main():
    input_file = 'data.txt'
    output_file = 'result.txt'

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
        write_result(output_file, result)

if __name__ == "__main__":
    main()