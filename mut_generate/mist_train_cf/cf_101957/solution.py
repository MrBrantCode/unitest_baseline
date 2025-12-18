"""
QUESTION:
Write a function `age_group` that determines the age group of a person based on their age. The age groups are defined as follows:
- Less than 13: Child
- 13-19: Teenager
- 20-64: Adult
- 65-79: Senior
- 80-99: Elderly
- 100 or greater: Centenarian

The function should take an integer age as input and return the corresponding age group.
"""

def age_group(age):
    """
    This function determines the age group of a person based on their age.

    Args:
        age (int): The age of the person.

    Returns:
        str: The age group of the person.
    """
    if age < 13:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age <= 64:
        return "Adult"
    elif 65 <= age <= 79:
        return "Senior"
    elif 80 <= age <= 99:
        return "Elderly"
    else:
        return "Centenarian"