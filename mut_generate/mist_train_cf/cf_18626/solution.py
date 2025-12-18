"""
QUESTION:
Write a function called `character_frequency` that calculates the frequency of uppercase, lowercase, and other characters in a given string, excluding non-alphabet characters. The function should return a dictionary containing the frequency of each type as a percentage of the total number of alphabet characters in the string.
"""

def character_frequency(string):
    """
    This function calculates the frequency of uppercase, lowercase, and other characters 
    in a given string, excluding non-alphabet characters. It returns a dictionary 
    containing the frequency of each type as a percentage of the total number of 
    alphabet characters in the string.
    
    Parameters:
    string (str): The input string for which the character frequency is calculated.
    
    Returns:
    dict: A dictionary containing the frequency of uppercase, lowercase, and other 
    characters as percentages.
    """
    
    uppercase_count = 0
    lowercase_count = 0
    total_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

        if char.isalpha():
            total_count += 1

    uppercase_percentage = (uppercase_count / total_count) * 100 if total_count != 0 else 0
    lowercase_percentage = (lowercase_count / total_count) * 100 if total_count != 0 else 0
    other_percentage = 100 - uppercase_percentage - lowercase_percentage

    return {
        'Uppercase': uppercase_percentage,
        'Lowercase': lowercase_percentage,
        'Other': other_percentage
    }