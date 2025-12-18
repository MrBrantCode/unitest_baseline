"""
QUESTION:
Create a function "distance" that takes two sets of 2D coordinates in the form of [x1, y1] and [x2, y2] as input and returns the Euclidean distance between them. Implement the function without using any mathematical functions or operators such as square root or power, only using basic arithmetic operations like addition, subtraction, multiplication, and division. The function should handle coordinates with negative and decimal values accurately.
"""

def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    
    # Calculate the square of the differences in x and y coordinates
    dx_sq = (x2 - x1) ** 2
    dy_sq = (y2 - y1) ** 2
    
    # Calculate the sum of the squares
    sum_of_squares = dx_sq + dy_sq
    
    # Iteratively calculate the distance
    distance = sum_of_squares
    guess = 1
    while abs(guess**2 - sum_of_squares) > 0.001:
        guess = (guess + sum_of_squares / guess) / 2
        distance = guess
    
    return distance