"""
QUESTION:
Write a function named `calculate_probability` that takes three integers representing the side lengths of a triangle as input and returns the probability of an ant exiting the triangle along its longest side. The probability should be calculated as the ratio of the longest side to the perimeter of the triangle, and the result should be rounded to 10 decimal places.
"""

def calculate_probability(side_a, side_b, side_c):
    """
    Calculate the probability of an ant exiting the triangle along its longest side.

    Args:
    side_a (int): The length of the first side of the triangle.
    side_b (int): The length of the second side of the triangle.
    side_c (int): The length of the third side of the triangle.

    Returns:
    float: The probability of the ant exiting along the longest side, rounded to 10 decimal places.
    """
    # Determine the longest side
    longest_side = max(side_a, side_b, side_c)
    
    # Calculate probability
    probability = longest_side / (side_a + side_b + side_c)
    
    # Return probability rounded to 10 decimal places
    return round(probability, 10)