"""
QUESTION:
Write a function called `calculate_sum_of_ages` that takes a dictionary with 'name' and 'age' keys as input. The function should calculate the sum of ages of people whose names start with 'J', are above 18 years old, and have an odd age. Implement the solution using a single loop and utilize list comprehension and lambda functions.
"""

def calculate_sum_of_ages(dictionary):
    """
    Calculate the sum of ages of people whose names start with 'J', are above 18 years old, and have an odd age.

    Args:
        dictionary (dict): A dictionary with 'name' and 'age' keys.

    Returns:
        int: The sum of ages.
    """
    # Filter the names starting with 'J' and odd ages using list comprehension
    filtered_data = [(name, age) for name, age in zip(dictionary['name'], dictionary['age']) if name.startswith('J') and age > 18 and age % 2 != 0]

    # Calculate the sum of ages using lambda function
    sum_of_ages = sum(map(lambda x: x[1], filtered_data))

    return sum_of_ages