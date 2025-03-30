#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 00:46:59 2025

@author: lindakovacs
"""

from collections import Counter

# Simulated Roulette Game (without random numbers) with user bets and a simulated spin.
def roulette_game(spins):
    numbers = list(range(37))  # Numbers 0 to 36 on the roulette wheel
    start_position = 7  # Arbitrary starting position (can be any valid number)

    # Formula: Determine stopping position using modular arithmetic
    stop_position = (start_position + (spins * 3)) % 37 # 3 is an arbitrary number

    return numbers[stop_position]  # Return the final number

# Function to calculate the mode of a list
def calculate_mode(numbers):
    count = Counter(numbers)
    mode = count.most_common(1)[0][0]
    return mode

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

# Display the final results
print(f"\nWinning number: {winning_number}")

if __name__ == "__main__":
    roulette_game(spins)


# Sort Code
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Mar  3 00:46:59 2025

# @author: lindakovacs
# """

# from collections import Counter

# # Simulated Roulette Game (without random numbers) with user bets and a simulated spin.
# def roulette_game(spins):
#     numbers = list(range(37))  # Numbers 0 to 36 on the roulette wheel
#     start_position = 7  # Arbitrary starting position (can be any valid number)

#     # Formula: Determine stopping position using modular arithmetic
#     stop_position = (start_position + (spins * 3)) % 37 # 3 is an arbitrary number

#     return numbers[stop_position]  # Return the final number

# # Function to calculate the mode of a list
# def calculate_mode(numbers):
#     count = Counter(numbers)
#     mode = count.most_common(1)[0][0]
#     return mode

# # Ask the user to place a bet
# while True:
#     try:
#         bet = int(input("Place your bet on a number (0-36): "))
#         if 0 <= bet <= 36:
#             break
#         else:
#             print("Invalid input! Enter a number between 0 and 36.")
#     except ValueError:
#         print("Invalid input! Enter a valid number.")

# # Ask the user for the number of spins
# while True:
#     try:
#         spins = int(input("Enter the number of times the roulette should spin: "))
#         if spins > 0:
#             break
#         else:
#             print("Number of spins must be greater than zero.")
#     except ValueError:
#         print("Invalid input! Enter a valid number.")

# # Lists to keep track of the winning numbers and bets
# winning_numbers = []
# bets = []

# # Run the roulette game for 20 rounds
# for _ in range(20):
#     # Simulate the roulette spinning
#     print("\nRoulette spinning...", end=" ")

#     # Get the final stopping number
#     winning_number = roulette_game(spins)
#     winning_numbers.append(winning_number)
#     bets.append(bet)

#     # Display the result
#     print(f"\nThe ball landed on: {winning_number}")

#     # Check if the user won
#     if bet == winning_number:
#         print("🎉 Congratulations! You won!")
#     else:
#         print("😞 Better luck next time!")

# # Calculate the mode of the winning numbers
# mode_winning_number = calculate_mode(winning_numbers)

# # Calculate the total wins and losses
# total_wins = sum(1 for i in range(20) if bets[i] == winning_numbers[i])
# total_losses = 20 - total_wins

# # Display the final results
# print(f"\nMode of the winning numbers: {mode_winning_number}")
# print(f"Total wins: {total_wins}")
# print(f"Total losses: {total_losses}")

# if __name__ == "__main__":
#     roulette_game(spins)

# from collections import Counter

# # Simulated Roulette Game (without random numbers) with user bets and a simulated spin.
# def roulette_game(spins):
#     numbers = list(range(37))  # Numbers 0 to 36 on the roulette wheel
#     start_position = 7  # Arbitrary starting position (can be any valid number)

#     # Formula: Determine stopping position using modular arithmetic
#     stop_position = (start_position + (spins * 3)) % 37  # 3 is an arbitrary number

#     return numbers[stop_position]  # Return the final number

# # Function to calculate the mode of a list
# def calculate_mode(numbers):
#     count = Counter(numbers)
#     mode = count.most_common(1)[0][0]
#     return mode

# # Function to sort results by winning number
# def sort_results(results):
#     return sorted(results, key=lambda x: x[0])

# # Ask the user to place a bet
# while True:
#     try:
#         bet = int(input("Place your bet on a number (0-36): "))
#         if 0 <= bet <= 36:
#             break
#         else:
#             print("Invalid input! Enter a number between 0 and 36.")
#     except ValueError:
#         print("Invalid input! Enter a valid number.")

# # Ask the user for the number of spins
# while True:
#     try:
#         spins = int(input("Enter the number of times the roulette should spin: "))
#         if spins > 0:
#             break
#         else:
#             print("Number of spins must be greater than zero.")
#     except ValueError:
#         print("Invalid input! Enter a valid number.")

# # Lists to keep track of the winning numbers and bets
# results = []

# # Run the roulette game for 100 runs
# for _ in range(100):
#     # Simulate the roulette spinning
#     print("\nRoulette spinning...", end=" ")
#     for i in range(spins):
#         print(f"{(7 + (i * 3)) % 37}", end=" ", flush=True)  # Simulating spinning effect

#     # Get the final stopping number
#     winning_number = roulette_game(spins)
#     results.append((winning_number, bet))

# # Sort the results by winning number
# sorted_results = sort_results(results)

# # Display the sorted results
# print("\nSorted Results (Winning Number, Bet):")
# for result in sorted_results:
#     print(result)

# # Calculate the mode of the winning numbers
# winning_numbers = [result[0] for result in results]
# mode_winning_number = calculate_mode(winning_numbers)

# # Calculate the total wins and losses
# total_wins = sum(1 for result in results if result[1] == result[0])
# total_losses = 100 - total_wins

# # Display the final results
# print(f"\nMode of the winning numbers: {mode_winning_number}")
# print(f"Total wins: {total_wins}")
# print(f"Total losses: {total_losses}")

# if __name__ == "__main__":
#     roulette_game(spins)