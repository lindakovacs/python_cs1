#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 14:55:31 2025

@author: lindakovacs
"""

import turtle as tl
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw

class PONG:

    def __init__(self):
        # Initialize player names
        self.left_player_name = input("Enter the name of the Left Player: ")
        self.right_player_name = input("Enter the name of the Right Player: ")

        # Upload player pictures using a file dialog
        self.left_player_image = self.get_player_image("Left Player")
        self.right_player_image = self.get_player_image("Right Player")

        # Score Variables initialization
        self.left_score = 0
        self.right_score = 0

        # Variables initialization
        self.create_window()
        self.display_player_images()
        self.leftpaddle()
        self.rightpaddle()
        self.create_ball()
        self.create_score_display()  # Create score display
        self.keys()
        self.game()  # Start the game

    def get_player_image(self, player_name):
        # Use tkinter to open a file dialog for selecting the player's image
        print(f"Select a profile picture for {player_name} (PNG format only).")
        root = Tk()
        root.withdraw()  # Hide the root tkinter window
        file_path = askopenfilename(filetypes=[("PNG files", "*.png")])
        root.destroy()  # Close the tkinter window
        if not file_path:
            print(f"No file selected for {player_name}. Exiting.")
            exit()
        return file_path

    def create_window(self):
        self.root = tl.Screen()
        self.root.title("PONG GAME by PythonGeeks")
        self.root.bgcolor("green")
        self.root.setup(width=600, height=400)
        self.root.tracer(0)

        # Position the game window at the center of the screen
        canvas = self.root.getcanvas()
        screen_width = canvas.winfo_screenwidth()
        screen_height = canvas.winfo_screenheight()

        # Calculate the position to center the window
        window_width = 600
        window_height = 400
        position_x = (screen_width - window_width) // 2
        position_y = (screen_height - window_height) // 2 - 100  # Adjust to place above VSCode

        canvas.master.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    def display_player_images(self):
        # Display the left player's image
        self.left_player_turtle = tl.Turtle()
        self.left_player_turtle.penup()
        self.left_player_turtle.hideturtle()
        self.left_player_turtle.goto(-350, 370)  # Position the left image above the score
        self.left_player_image_tk = self.display_circular_image(self.left_player_turtle, self.left_player_image)

        # Display the right player's image
        self.right_player_turtle = tl.Turtle()
        self.right_player_turtle.penup()
        self.right_player_turtle.hideturtle()
        self.right_player_turtle.goto(-250, 370)  # Position the right image above the score
        self.right_player_image_tk = self.display_circular_image(self.right_player_turtle, self.right_player_image)

    def display_circular_image(self, turtle_obj, image_path):
        # Use Pillow to crop the image into a circle and display it
        canvas = self.root.getcanvas()
        img = Image.open(image_path).convert("RGBA")
        img = img.resize((50, 50))  # Resize the image to fit the game window

        # Create a circular mask
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

        # Apply the mask to the image
        circular_img = Image.new("RGBA", img.size)
        circular_img.paste(img, (0, 0), mask)

        # Convert the image to a format compatible with tkinter
        tk_img = ImageTk.PhotoImage(circular_img)

        # Correct the positioning of the image
        canvas_x = turtle_obj.xcor() + self.root.window_width() // 2
        canvas_y = self.root.window_height() // 2 - turtle_obj.ycor()
        canvas.create_image(canvas_x, canvas_y, image=tk_img)

        return tk_img  # Return the PhotoImage object to maintain a reference

    def leftpaddle(self):
        self.left_paddle = tl.Turtle()
        self.left_paddle.speed(0)
        self.left_paddle.shape('square')
        self.left_paddle.color('purple')
        self.left_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.left_paddle.penup()
        self.left_paddle.goto(-280, 0)

    def rightpaddle(self):
        self.right_paddle = tl.Turtle()
        self.right_paddle.speed(0)
        self.right_paddle.shape('square')
        self.right_paddle.color('blue')
        self.right_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.right_paddle.penup()
        self.right_paddle.goto(280, 0)

    def create_ball(self):
        self.ball = tl.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('orange')
        self.ball.penup()
        self.ball.goto(5, 5)
        self.ball_direction_x = 0.2
        self.ball_direction_y = 0.2

    def create_score_display(self):
        self.score_display = tl.Turtle()
        self.score_display.speed(0)
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 120)  # Adjusted position of the score display (below the images)
        self.update_score_display()  # Update display initially

    def update_score_display(self):
        self.score_display.clear()  # Clear previous score
        self.score_display.write(f"{self.left_player_name} {self.left_score} : {self.right_score} {self.right_player_name}",
                                 align="center", font=("Courier", 24, "normal"))

    def left_paddle_up(self):
        y = self.left_paddle.ycor()
        y = y + 20
        self.left_paddle.sety(y)

    def left_paddle_down(self):
        y = self.left_paddle.ycor()
        y = y - 20
        self.left_paddle.sety(y)

    def right_paddle_up(self):
        y = self.right_paddle.ycor()
        y = y + 20
        self.right_paddle.sety(y)

    def right_paddle_down(self):
        y = self.right_paddle.ycor()
        y = y - 20
        self.right_paddle.sety(y)

    def keys(self):
        self.root.listen()
        self.root.onkeypress(self.left_paddle_up, "w")
        self.root.onkeypress(self.left_paddle_down, "s")
        self.root.onkeypress(self.right_paddle_up, "Up")
        self.root.onkeypress(self.right_paddle_down, "Down")

    def game(self):
        while True:
            self.root.update()

            # Move the ball
            self.ball.setx(self.ball.xcor() + self.ball_direction_x)
            self.ball.sety(self.ball.ycor() + self.ball_direction_y)

            # Check for collisions with the top and bottom walls
            if self.ball.ycor() > 190:
                self.ball.sety(190)
                self.ball_direction_y *= -1

            if self.ball.ycor() < -190:
                self.ball.sety(-190)
                self.ball_direction_y *= -1

            # Check for paddle collisions
            if (self.ball.xcor() > 260 and self.ball.xcor() < 270) and (self.ball.ycor() < self.right_paddle.ycor() + 40 and self.ball.ycor() > self.right_paddle.ycor() - 40):
                self.ball.setx(260)
                self.ball_direction_x *= -1

            if (self.ball.xcor() < -260 and self.ball.xcor() > -270) and (self.ball.ycor() < self.left_paddle.ycor() + 40 and self.ball.ycor() > self.left_paddle.ycor() - 40):
                self.ball.setx(-260)
                self.ball_direction_x *= -1

            # Check if the ball went past the edge (scoring)
            if self.ball.xcor() > 280:  # Ball went past right edge
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1
                self.left_score += 1  # Increment left score
                self.update_score_display()

            if self.ball.xcor() < -280:  # Ball went past left edge
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1
                self.right_score += 1  # Increment right score
                self.update_score_display()

            # Check if a player has won
            if self.left_score == 7:
                self.display_winner(f"{self.left_player_name} Wins!!")
                break
            elif self.right_score == 7:
                self.display_winner(f"{self.right_player_name} Wins!!")
                break

        # Ask if players want to play another round
        play_again = self.root.textinput("Game Over", "Do you want to play again? (yes/no)")
        if play_again and play_again.lower() == "yes":
            self.reset_game()
        else:
            self.root.bye()

    def display_winner(self, message):
        # Display the winner on the game window
        self.score_display.clear()
        self.score_display.write(message, align="center", font=("Courier", 36, "bold"))

    def reset_game(self):
        # Reset the game state for a new round
        self.left_score = 0
        self.right_score = 0
        self.update_score_display()
        self.ball.goto(0, 0)
        self.ball_direction_x = 0.2
        self.ball_direction_y = 0.2
        self.game()

def main():
    PONG()

if __name__ == '__main__':
    main()