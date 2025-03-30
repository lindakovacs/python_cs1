#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:34:32 2025

@author: lindakovacs
"""

# Simulated Roulette Game (without random numbers) with user bets and a simulated spin.
def roulette_game(spins):
    numbers = list(range(37))  # Numbers 0 to 36 on the roulette wheel
    start_position = 7  # Arbitrary starting position (can be any valid number)

    # Formula: Determine stopping position using modular arithmetic
    stop_position = (start_position + (spins * 3)) % 37 # 3 is an arbitrary number

    return numbers[stop_position]  # Return the final number

# Ask the user to place a bet
while True:
    try:
        bet = int(input("Place your bet on a number (0-36): "))
        if 0 <= bet <= 36:
            break
        else:
            print("Invalid input! Enter a number between 0 and 36.")
    except ValueError:
        print("Invalid input! Enter a valid number.")

# Ask the user for the number of spins
while True:
    try:
        spins = int(input("Enter the number of times the roulette should spin: "))
        if spins > 0:
            break
        else:
            print("Number of spins must be greater than zero.")
    except ValueError:
        print("Invalid input! Enter a valid number.")

# Simulate the roulette spinning
print("\nRoulette spinning...", end=" ")
for i in range(spins):
    print(f"{(7 + (i * 3)) % 37}", end=" ", flush=True)  # Simulating spinning effect

# Get the final stopping number
winning_number = roulette_game(spins)

# Display the result
print(f"\nThe ball landed on: {winning_number}")

# Check if the user won
if bet == winning_number:
    print("🎉 Congratulations! You won!")
else:
    print("😞 Better luck next time!")

if __name__ == "__main__":
    roulette_game(spins)


