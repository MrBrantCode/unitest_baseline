"""
QUESTION:
Implement a function calculate_distance(x1: int, y1: int, x2: int, y2: int) -> float that takes in four integers representing the coordinates of two points and returns their Euclidean distance as a float. The Euclidean distance is defined as the square root of the sum of the squares of the differences between corresponding coordinates. You can assume that the inputs will be valid integers and you should not use any built-in functions or libraries to calculate the square root.
"""

def calculate_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    difference_x = x2 - x1
    difference_y = y2 - y1
    sum_of_squares = difference_x**2 + difference_y**2
    euclidean_distance = sum_of_squares**0.5
    return euclidean_distance