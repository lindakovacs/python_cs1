#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:46:29 2025

@author: lindakovacs
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def sqft_to_sqm(sqft):
    return sqft * 0.092903

def sqm_to_sqft(sqm):
    return sqm / 0.092903

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

def temperature_conversion():
    print("Temperature Conversion Program")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    elif choice == '2':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        except ValueError:
            print("Invalid input! Enter a valid number.")
    else:
        print("Invalid choice. Enter 1 or 2.")

def area_conversion():
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

def area_calculation():
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

def main():
    print("Main Menu")
    print("1. Temperature Conversion")
    print("2. Area Conversion")
    print("3. Area Calculation")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        temperature_conversion()
    elif choice == '2':
        area_conversion()
    elif choice == '3':
        area_calculation()
    else:
        print("Invalid choice. Enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
