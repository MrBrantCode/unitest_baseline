"""
QUESTION:
Write a function `compute_average_height` that takes a list of heights in centimeters as input. The function should return the average height, ignoring heights outside the range 100-200 cm and negative heights. If the input list is empty or no valid heights are found, the function should return 0.
"""

def compute_average_height(heights):
    if not heights:  # If the list is empty, return 0
        return 0

    valid_heights = [height for height in heights if 100 <= height <= 200 and height >= 0]

    if not valid_heights:  # If no valid heights, return 0
        return 0

    average_height = sum(valid_heights) / len(valid_heights)  # Calculate average height
    return average_height