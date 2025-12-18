"""
QUESTION:
Write a function `calculate_paper_towels_per_room` that determines the number of paper towels per room given a total number of paper towels and the number of rooms. The function should take two parameters: `total_paper_towels` and `rooms`. It should return the number of paper towels per room, calculated by dividing the total number of paper towels by the number of rooms.
"""

def calculate_paper_towels_per_room(total_paper_towels, rooms):
    """
    Calculate the number of paper towels per room.

    Args:
        total_paper_towels (int): The total number of paper towels.
        rooms (int): The number of rooms.

    Returns:
        float: The number of paper towels per room.
    """
    return total_paper_towels / rooms