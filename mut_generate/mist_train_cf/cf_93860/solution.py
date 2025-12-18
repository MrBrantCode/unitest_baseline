"""
QUESTION:
Create a function `sum_odd_ages` that calculates the sum of ages from a given dictionary where names start with 'J', ages are above 18, and ages are odd. The dictionary contains two lists: 'name' and 'age', where each index corresponds to the same person's name and age, respectively.
"""

def sum_odd_ages(dictionary):
    """
    Calculate the sum of ages from a given dictionary where names start with 'J', 
    ages are above 18, and ages are odd.
    
    Parameters:
    dictionary (dict): A dictionary with 'name' and 'age' lists.
    
    Returns:
    int: The sum of ages of people whose names start with 'J' and satisfy the given conditions.
    """
    return sum(age for name, age in zip(dictionary['name'], dictionary['age']) 
               if name.startswith('J') and age > 18 and age % 2 != 0)