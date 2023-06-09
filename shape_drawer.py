# Simple shape drawer that draws a square, triangle, or circle based on user input
# Author: Sajith Madhusankha
# Created: 2023-06-09
# Try to improve the code by adding more shapes and colors

import turtle

# Initialize the turtle screen
screen = turtle.Screen()

# Create a turtle object
builder = turtle.Turtle()

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        builder.forward(side_length)
        builder.right(90)

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        builder.forward(side_length)
        builder.right(120)

# Function to draw a circle
def draw_circle(radius):
    builder.circle(radius)

# Set the speed of drawing
builder.speed(2)

# Welcome message
print("****Welcome to the shape drawer!***")
print("You can draw a square, triangle, or circle.")

# Ask about the shape to draw
shape = input("Enter the shape to draw: ")

# Check the shape and draw accordingly
if shape == "square":
    # Ask for the side length
    side_length = float(input("Enter the side length for the square: "))

    # Call the function to draw the square
    draw_square(side_length)

    # Move the turtle to a new position
    builder.penup()
    builder.goto(side_length + 50, 0)
    builder.pendown()
    
elif shape == "triangle":
    # Ask for the side length
    side_length = float(input("Enter the side length for the triangle: "))

    # Call the function to draw the triangle
    draw_triangle(side_length)

    # Move the turtle to a new position
    builder.penup()
    builder.goto((side_length + 50) * 2, 0)
    builder.pendown()

elif shape == "circle":
    # Ask for the radius
    radius = float(input("Enter the radius for the circle: "))

    # Call the function to draw the circle
    draw_circle(radius)

# If the shape is not valid
else:
    print("Invalid shape entered")