"""
QUESTION:
Write a function called `sum_of_ages` that takes a dictionary as input where the dictionary has two keys 'name' and 'age'. The function should return the sum of the ages of people whose names start with the letter 'J' and are above 18 years old.
"""

def entrance(people):
    """
    Calculate the sum of the ages of people whose names start with the letter 'J' and are above 18 years old.

    Args:
        people (dict): A dictionary with 'name' and 'age' keys.

    Returns:
        int: The sum of ages of people whose names start with 'J' and are above 18 years old.
    """
    return sum(age for name, age in zip(people['name'], people['age']) if name[0].lower() == 'j' and age > 18)