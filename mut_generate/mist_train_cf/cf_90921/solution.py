"""
QUESTION:
Write a function `convert_to_dictionary` that takes a list of strings as input and returns a dictionary. The dictionary should have numbers as keys starting from 1 in ascending order, and the corresponding values should be the input strings converted to uppercase. The function should only include strings with at least 3 characters and at least one vowel in the resulting dictionary.
"""

def convert_to_dictionary(lst):
    """
    This function takes a list of strings as input, filters the strings based on the length and presence of vowels,
    and returns a dictionary with the filtered strings in uppercase and keys starting from 1.

    Parameters:
    lst (list): A list of strings.

    Returns:
    dict: A dictionary with filtered strings in uppercase and keys starting from 1.
    """
    vowels = ['A', 'E', 'I', 'O', 'U']  # List of vowels
    result = {}  # Empty dictionary to store the result
    count = 1  # Starting number for keys
    
    for string in lst:
        # Check if the string has at least 3 characters and contains at least one vowel
        if len(string) >= 3 and any(vowel in string.upper() for vowel in vowels):
            result[count] = string.upper()  # Assign the string in uppercase as value
            count += 1  # Increment the key value
            
    return result