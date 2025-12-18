"""
QUESTION:
Write a function named `calculate_green_balls` to find out how many green-colored soccer balls are included in a collection. The collection contains a total number of balls, a certain number of which are white, and the remaining balls are equally divided among three colors: blue, pink, and green. The function takes two parameters, `total_balls` and `white_balls`, and returns the number of green-colored soccer balls.
"""

def calculate_green_balls(total_balls, white_balls):
    """
    Calculate the number of green-colored soccer balls in a collection.

    The collection contains a total number of balls, a certain number of which are white,
    and the remaining balls are equally divided among three colors: blue, pink, and green.

    Args:
        total_balls (int): The total number of balls in the collection.
        white_balls (int): The number of white balls in the collection.

    Returns:
        int: The number of green-colored soccer balls.
    """
    remaining_balls = total_balls - white_balls
    balls_per_color = remaining_balls / 3
    return balls_per_color