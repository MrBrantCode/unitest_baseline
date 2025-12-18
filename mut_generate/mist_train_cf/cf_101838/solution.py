"""
QUESTION:
Write a function named `calculate_mozart_age` that takes two integers representing Mozart's birth year and the year he composed Symphony No. 41 as input. The function should return Mozart's age at the time of composition.
"""

def calculate_mozart_age(birth_year, composition_year):
    """
    Calculate Mozart's age at the time of composition.

    Args:
        birth_year (int): Mozart's birth year.
        composition_year (int): The year Mozart composed Symphony No. 41.

    Returns:
        int: Mozart's age at the time of composition.
    """
    return composition_year - birth_year