"""
QUESTION:
Implement the function is_star_jumping_high_enough that takes two parameters, star_height and min_height, and returns True if the absolute difference between star_height and min_height is 5 or more, and False otherwise. The function must handle negative and decimal values for both parameters and have a time complexity of O(1).
"""

def is_star_jumping_high_enough(star_height, min_height):
    return abs(star_height - min_height) >= 5