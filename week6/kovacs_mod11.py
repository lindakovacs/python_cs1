#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 01:08:07 2025

@author: lindakovacs
"""

def read_first_line(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
    return first_line

def count_spaces_in_paragraph(file_path):
    with open(file_path, 'r') as file:
        paragraph = file.read().split('\n\n')[0]  # Read the first paragraph
    return paragraph.count(' ')

def add_first_line_to_file(source_file, target_file):
    first_line = read_first_line(source_file)
    with open(target_file, 'a') as file:
        file.write(first_line + '\n')

def display_file_contents(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    print(contents)

def main():
    py_file_ops_path = 'pyFileOps.txt'
    american_thanksgiving_path = 'American_Thanksgiving.txt'

    # (a) Read and print the first line in the first paragraph of the file pyFileOps.txt
    first_line = read_first_line(py_file_ops_path)
    print(f"First line in the first paragraph of {py_file_ops_path}:")
    print(first_line)
    print()

    # (b) Count the number of empty spaces in the first paragraph
    space_count = count_spaces_in_paragraph(py_file_ops_path)
    print(f"Number of empty spaces in the first paragraph of {py_file_ops_path}: {space_count}")
    print()

    # (c) Open the file American_Thanksgiving.txt and add the first line of the file pyFileOps.txt to it
    add_first_line_to_file(py_file_ops_path, american_thanksgiving_path)

    # Display the contents of the file American_Thanksgiving.txt
    print(f"Contents of {american_thanksgiving_path}:")
    display_file_contents(american_thanksgiving_path)

if __name__ == "__main__":
    main()

