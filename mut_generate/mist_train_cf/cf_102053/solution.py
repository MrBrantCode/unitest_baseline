"""
QUESTION:
Write a function `determine_age_group` that takes an integer age as input and returns a string describing the corresponding age group. The age groups are: "minor" (below 18), "adult" (18-60), "senior citizen" (61-100), and "centenarian" (above 100). If the input is not a valid integer, the function should return "Invalid age input."
"""

def determine_age_group(age):
    """
    This function determines the age group of a given age.

    Args:
        age (int): The age of the person.

    Returns:
        str: A string describing the corresponding age group.
    """
    try:
        age = int(age)
        if age < 0:
            return "Invalid age input."
        elif age < 18:
            return "You are a minor."
        elif age <= 60:
            return "You are an adult."
        elif age <= 100:
            return "You are a senior citizen."
        else:
            return "You are a centenarian."
    except ValueError:
        return "Invalid age input."