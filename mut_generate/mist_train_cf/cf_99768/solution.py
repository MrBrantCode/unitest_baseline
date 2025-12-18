"""
QUESTION:
Write a function named `calculate_age` that calculates a person's age given their birth year and the year they performed a certain activity. The function should take two parameters: `birth_year` and `composition_year`, both integers, and return the calculated age as an integer. The function should not take into account the exact dates of birth and composition, only the years.
"""

def calculate_age(birth_year, composition_year):
    """
    Calculate a person's age given their birth year and the year they performed a certain activity.

    Args:
        birth_year (int): The year the person was born.
        composition_year (int): The year the person performed the activity.

    Returns:
        int: The calculated age.
    """
    return composition_year - birth_year