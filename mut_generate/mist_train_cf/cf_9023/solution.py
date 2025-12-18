"""
QUESTION:
Write a function named `age_group` that takes an integer age as input and returns the corresponding age group. 
- If the age is less than 13, return "Child".
- If the age is between 13 and 19 (both inclusive), return "Teenager".
- If the age is between 20 and 64 (both inclusive), return "Adult".
- If the age is 65 or greater, return "Senior".
The function should not take any other inputs besides the age.
"""

def age_group(age: int) -> str:
    """
    This function takes an integer age as input and returns the corresponding age group.
    
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
    else:
        return "Senior"