import time

def pause(duration=2.0):
    """Pauses Python for a set amount of time, defaulting to 2 seconds."""
    time.sleep(duration)

"""Exercise 5.14.2"""
now = time.time()

def hr_calc():
    time_h = int(((now % 31536000) - (275 * 86400)) / 86400)
    return time_h

def min_calc():
    time_m = int((((now % 31536000) - (275 * 86400)) % 86400)) # TODO: Why is it not rounding
    return time_m

print(f"It has been {now//(60*60*24*365)} years since 1970.")
print(f"The time is now {hr_calc()}:{min_calc()} on October 01, 2024") # TODO: what.

"""Exercise 5.14.3"""
def is_triangle(s1, s2, s3):
    print("No") if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2 else print("Yes")

is_triangle(1, 2, 3) # yes
is_triangle(1, 2, 4) # no

"""Exercise 5.14.4"""
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
"""
Frame (Global) 'Recurse' --> Function recurse(n, s)
Function recurse(3, 0)
Function recurse(2, 3)
Function recurse(1, 5)
Function recurse(0, 6) --> Return value = None (Printed Value = 6)
"""

"""Exercise 5.14.5"""
from turtle import *
import turtle
speed = 10
def draw(length):
    angle = 50
    factor = 0.6
    if length > 5:
        forward(length) # forward length
        left(angle) # left 50 degrees
        draw(factor * length) # draws a branch of a fractal at 60% of the scale of the length
        right(2 * angle) # right 100 degrees
        draw(factor * length) # draws a branch of a fractal at 60% of the scale of the length
        left(angle) # left 50 degrees
        back(length) # backward length
        # the recursive nature of the code reduces the length until it is less than 5 to end it

draw(20)
pause()
clear()

"""Exercise 5.14.6"""
def koch(length):
    if length < 5:
        forward(length)
    else:
        koch(length/3)
        left(60)
        koch(length/3)
        right(120)
        koch(length/3)
        left(60)
        koch(length/3)

def fractal(deg=60):
    n = 360 // deg
    for _ in range(n):
            koch(120)
            right(deg)

fractal()
pause()
clear()

"""Exercise 5.14.7"""
from turtle import *


def draw_triangle(points, color):
    fillcolor(color)
    begin_fill()
    for point in points:
        goto(point)
    end_fill()


def draw_triangle(points, color):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for point in points:
        turtle.goto(point)
    turtle.goto(points[0])  # Close the triangle
    turtle.end_fill()

def sierpinski_triangle(order, points):
    if order == 0:
        draw_triangle(points, "blue")
    else:
        # Calculate the midpoints of each side of the triangle
        midpoints = [
            ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2),
            ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2),
            ((points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2)
        ]
        # Recursively draw the three smaller triangles
        sierpinski_triangle(order - 1, [points[0], midpoints[0], midpoints[2]])
        sierpinski_triangle(order - 1, [points[1], midpoints[0], midpoints[1]])
        sierpinski_triangle(order - 1, [points[2], midpoints[1], midpoints[2]])

def main():
    turtle.speed(0)  # Fastest drawing speed
    turtle.bgcolor("white")

    # Define the vertices of the initial triangle
    points = [(-200, -150), (0, 200), (200, -150)]

    # Draw the Sierpiński triangle of order 4
    sierpinski_triangle(4, points)

    turtle.done()

if __name__ == "__main__":
    main()