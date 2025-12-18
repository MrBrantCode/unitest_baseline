"""
QUESTION:
Create a function called `calculate_square_properties` that takes the side length of a square as input and returns a dictionary containing the perimeter and area of the square, the perimeter and area of the four smaller squares created by dividing the original square into four equal parts, and the total area of the larger square not covered by the smaller squares. The function should not take any additional arguments other than the side length of the square.
"""

def calculate_square_properties(side_length):
    """
    Calculate the perimeter and area of a square, the perimeter and area of the four smaller squares 
    created by dividing the original square into four equal parts, and the total area of the larger 
    square not covered by the smaller squares.

    Args:
        side_length (float): The side length of the square.

    Returns:
        dict: A dictionary containing the perimeter and area of the square, the perimeter and area 
        of the four smaller squares, and the total area of the larger square not covered by the 
        smaller squares.
    """

    # Calculate the perimeter and area of the large square
    large_square_perimeter = 4 * side_length
    large_square_area = side_length ** 2
    
    # Calculate the perimeter and area of each small square
    small_square_side_length = side_length / 2
    small_square_perimeter = 4 * small_square_side_length
    small_square_area = small_square_side_length ** 2
    
    # Calculate the total area of the larger square that is not covered by the smaller squares
    total_area = large_square_area - (4 * small_square_area)
    
    # Return the results in a dictionary
    return {
        "large_square": {"perimeter": large_square_perimeter, "area": large_square_area},
        "small_square": {"perimeter": small_square_perimeter, "area": small_square_area},
        "total_area_not_covered": total_area
    }