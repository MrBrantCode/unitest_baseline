"""
QUESTION:
Create a function `determine_age_group` that takes one argument, the age of a person, and prints the corresponding age group. The age groups are defined as: under 18 as "minor", 18 to 60 (inclusive) as "adult", and above 60 as "senior citizen". The function should handle non-integer age inputs and print "Invalid age input".
"""

def determine_age_group(age):
    """
    Prints the corresponding age group based on the input age.
    
    Args:
        age (int): The age of a person.
    
    Returns:
        str: The age group.
    """
    if not isinstance(age, int):
        return "Invalid age input"
    if age < 18:
        return "You are a minor."
    elif 18 <= age <= 60:
        return "You are an adult."
    elif age > 60:
        return "You are a senior citizen."