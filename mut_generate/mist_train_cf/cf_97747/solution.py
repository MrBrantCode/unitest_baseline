"""
QUESTION:
Calculate the perimeter of a square inscribed in a circle with a diameter of 15 centimeters. The function should be named calculate_perimeter. Assume the square is cut into four equal smaller squares and also return the total perimeter of those smaller squares combined.
"""

import math

def calculate_perimeter(diameter):
    """
    Calculate the perimeter of a square inscribed in a circle and 
    the total perimeter of four smaller squares when the original 
    square is cut into four equal parts.

    Args:
    diameter (float): The diameter of the circle.

    Returns:
    tuple: A tuple containing the perimeter of the square and the 
    total perimeter of the smaller squares.
    """
    # Calculate the side length of the square using the Pythagorean theorem
    side_length = math.sqrt((diameter ** 2) / 2)
    
    # Calculate the perimeter of the square
    square_perimeter = 4 * side_length
    
    # Calculate the side length and perimeter of each smaller square
    smaller_square_side_length = side_length / math.sqrt(2)
    smaller_square_perimeter = 4 * smaller_square_side_length
    
    # Calculate the total perimeter of the smaller squares
    total_smaller_squares_perimeter = 4 * smaller_square_perimeter
    
    return square_perimeter, total_smaller_squares_perimeter

# Function usage
square_perimeter, total_smaller_squares_perimeter = calculate_perimeter(15)