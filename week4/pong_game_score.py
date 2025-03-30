#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 21:41:43 2025

@author: lindakovacs
"""

import turtle as tl

class PONG:

    def __init__(self):

        # Score Variables initialization
        self.left_score = 0
        self.right_score = 0

        # Variables initialization
        self.create_window()
        self.leftpaddle()
        self.rightpaddle()
        self.create_ball()
        self.create_score_display()  # Create score display
        self.keys()
        self.game()  # Start the game

    def create_score_display(self): # Function to create score display
        self.score_display = tl.Turtle()
        self.score_display.speed(0)
        self.score_display.color("black")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 160)  # Position score display
        self.update_score_display()  # Update display initially

    def create_window(self):
        self.root = tl.Screen()
        self.root.title("PONG GAME by PythonGeeks")
        self.root.bgcolor("green")
        self.root.setup(width=600, height=400)
        self.root.tracer(0)

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

    def update_score_display(self): # Function to update the score display
        self.score_display.clear()  # Clear previous score
        self.score_display.write(f"Left: {self.left_score} Right: {self.right_score}", align="center", font=("Courier", 24, "normal"))

    def game(self):
        while True:
            self.root.update()

            self.ball.setx(self.ball.xcor() + self.ball_direction_x)
            self.ball.sety(self.ball.ycor() + self.ball_direction_y)

            if self.ball.ycor() > 190:
                self.ball.sety(190)
                self.ball_direction_y *= -1

            if self.ball.ycor() < -190:
                self.ball.sety(-190)
                self.ball_direction_y *= -1

            # 1. Check for paddle collisions FIRST
            # Improved paddle collision detection
            if (self.ball.xcor() > 260 and self.ball.xcor() < 270) and (self.ball.ycor() < self.right_paddle.ycor() + 40 and self.ball.ycor() > self.right_paddle.ycor() - 40):
                self.ball.setx(260)  # slightly adjust to prevent ball from getting stuck
                self.ball_direction_x *= -1

            if (self.ball.xcor() < -260 and self.ball.xcor() > -270) and (self.ball.ycor() < self.left_paddle.ycor() + 40 and self.ball.ycor() > self.left_paddle.ycor() - 40):
                self.ball.setx(-260)  # slightly adjust to prevent ball from getting stuck
                self.ball_direction_x *= -1

            # 2. Check if the ball went past the edge (scoring) AFTER collision check
            if self.ball.xcor() > 280: # Ball went past right edge
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1
                self.right_score += 1  # Increment right score
                self.update_score_display() # Update score display after scoring

            if self.ball.xcor() < -280: # Ball went past left edge
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1
                self.left_score += 1  # Increment left score
                self.update_score_display() # Update score display after scoring

def main():
    PONG()

if __name__ == '__main__':
    main()