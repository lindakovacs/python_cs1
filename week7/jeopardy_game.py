#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 21:06:49 2025

@author: lindakovacs
"""

import random

def display_menu():
    print("\nJeopardy Game Menu:")
    print("1. Play Game")
    print("2. Exit")

def display_categories(categories):
    print("\nCategories:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

def get_question(category, questions):
    question, answer = random.choice(list(questions[category].items()))
    return question, answer

def play_game(categories, questions):
    score = 0
    for _ in range(3):  # Play 3 rounds
        display_categories(categories)
        category_choice = int(input("Choose a category (1-3): ")) - 1
        category = categories[category_choice]
        question, answer = get_question(category, questions)
        print(f"\nCategory: {category}")
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("🎉 Congratulations! That's correct!")
            score += 1
        else:
            print(f"Incorrect! 😞 Better luck next time! The correct answer was: {answer}")
        # Ask if the user wants to continue or exit
        continue_choice = input("Do you want to continue playing? (yes/no): ").strip().lower()
        if continue_choice == 'no':
            break
    print(f"\nGame Over! Your final score is: {score}")

def main():
    categories = ["Science", "History", "Geography"]
    questions = {
        "Science": {
            "What is the chemical symbol for water?": "H2O",
            "What planet is known as the Red Planet?": "Mars",
            "What gas do plants absorb from the atmosphere?": "Carbon Dioxide"
        },
        "History": {
            "Who was the first President of the United States?": "George Washington",
            "In which year did the Titanic sink?": "1912",
            "Who discovered America?": "Christopher Columbus"
        },
        "Geography": {
            "What is the capital of France?": "Paris",
            "Which is the largest ocean on Earth?": "Pacific Ocean",
            "What is the longest river in the world?": "Nile"
        }
    }
    while True:
        display_menu()
        choice = input("Enter your choice (1-2): ")
        if choice == '1':
            play_game(categories, questions)
        elif choice == '2':
            print("Exiting Jeopardy Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

