#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:44:20 2025

@author: lindakovacs
"""

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_rectangle(length, width):
    return length * width

def area_of_circle(radius):
    import math
    return math.pi * radius ** 2

def area_of_square(side):
    return side ** 2

def area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def main():
    print("Area Calculation Program")
    print("1. Area of Triangle")
    print("2. Area of Rectangle")
    print("3. Area of Circle")
    print("4. Area of Square")
    print("5. Area of Trapezoid")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        try:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = area_of_triangle(base, height)
            print(f"The area of the triangle is {area:.2f}")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    elif choice == '2':
        try:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = area_of_rectangle(length, width)
            print(f"The area of the rectangle is {area:.2f}")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    elif choice == '3':
        try:
            radius = float(input("Enter the radius of the circle: "))
            area = area_of_circle(radius)
            print(f"The area of the circle is {area:.2f}")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    elif choice == '4':
        try:
            side = float(input("Enter the side of the square: "))
            area = area_of_square(side)
            print(f"The area of the square is {area:.2f}")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    elif choice == '5':
        try:
            base1 = float(input("Enter the first base of the trapezoid: "))
            base2 = float(input("Enter the second base of the trapezoid: "))
            height = float(input("Enter the height of the trapezoid: "))
            area = area_of_trapezoid(base1, base2, height)
            print(f"The area of the trapezoid is {area:.2f}")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    else:
        print("Invalid choice. Enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

