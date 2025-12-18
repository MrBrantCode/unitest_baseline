"""
QUESTION:
Given n number of people in a room, calculate the probability that any two people in that room have the same birthday (assume 365 days every year = ignore leap year). Answers should be two decimals unless whole (0 or 1) eg 0.05
"""

def calculate_birthday_probability(n: int) -> float:
    """
    Calculate the probability that any two people in a room of size n have the same birthday.

    Parameters:
    n (int): The number of people in the room.

    Returns:
    float: The probability that any two people have the same birthday, rounded to two decimal places.
    """
    if n < 2:
        return 0.0
    return round(1 - (364 / 365) ** (n * (n - 1) / 2), 2)