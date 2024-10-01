"""CIS12 CH6 Exercises"""
import math

"""Exercise 6.12.1"""

def compute_distance_ai(point1, point2):
    """
    Compute the Euclidean distance between two points in 2D space.

    Args:
    point1 (tuple): Coordinates of the first point (x1, y1).
    point2 (tuple): Coordinates of the second point (x2, y2).

    Returns:
    float: The distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Example usage:
#point_a = (3, 4)
#point_b = (6, 8)
#print("Distance:", compute_distance_ai(point_a, point_b))

def distance_human(x1, y1, x2, y2):
    #alternative; concise but not easy to read: distance = math.sqrt( (x2 - x1)**2 + (y2 - y1) ** 2)
    dx = (x2 - x1)
    dy = (y2 - y1)
    dsq = dx**2 + dy**2
    distance = math.sqrt(dsq)
#    print(distance)
    return distance

distance_human(3, 4, 6, 8)

"""Exercise 6.12.2"""

def hypt(a, b):
    c2 = a**2 + b**2
    c = math.sqrt(c2)
#    print(c)
    return c

hypt(7, 5)

"""Exercise 6.12.3"""

def is_between(x, y, z):
    if x < y < z or z < y < x:
        return True
    else:
        return False

is_between(6, 3, 7)

"""Exercise 6.12.4"""

def ackermann(m, n): # Weird recursion error.
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ackermann(m-1, 1)
    if m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))

"""I don't understand my own translation lol."""

ackermann(5, 5)
#print(ackermann(5, 5))

"""Exercise 6.12.5"""

def gcd(a, b):
#    if b == 0: return a
#    return gcd(b, a % b)
    while b != 0:
        r = a % b
        a, b = b, r
    return a

"""Couldn't figure the math out on this one, but I kinda understand what's happening here."""