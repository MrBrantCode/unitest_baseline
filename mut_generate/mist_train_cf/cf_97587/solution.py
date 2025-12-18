"""
QUESTION:
Write a function named `calculate_age` that calculates a person's age given their birth year and the year they accomplished something. The function should take two integer parameters, `birth_year` and `completion_year`, and return the calculated age as an integer. Assume that the `completion_year` is always after the `birth_year`.
"""

def calculate_age(birth_year, completion_year):
    """
    Calculate a person's age given their birth year and the year they accomplished something.

    Args:
    birth_year (int): The person's birth year.
    completion_year (int): The year the person accomplished something.

    Returns:
    int: The calculated age.
    """
    return completion_year - birth_year