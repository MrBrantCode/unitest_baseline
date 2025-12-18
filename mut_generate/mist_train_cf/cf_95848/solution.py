"""
QUESTION:
Write a function named `expand_strings` that takes a list of strings as input. The function should expand each string into a set of characters if it contains at least one vowel and does not contain any special characters or numbers. The function should return a list of tuples, where each tuple contains the original string and its corresponding set of characters sorted in descending order based on the number of vowels.
"""

def expand_strings(strings):
    """
    Expand strings into sets of characters if they contain at least one vowel and do not contain special characters or numbers.
    
    Args:
        strings (list): A list of strings.
    
    Returns:
        list: A list of tuples, where each tuple contains the original string and its corresponding set of characters sorted in descending order based on the number of vowels.
    """
    expanded_strings = []

    for string in strings:
        if any(char.isdigit() or not char.isalnum() for char in string):
            continue
        
        vowels = set(char.lower() for char in string if char.lower() in 'aeiou')
        if len(vowels) == 0:
            continue
        
        expanded_strings.append((string, vowels))

    expanded_strings.sort(key=lambda x: len(x[1]), reverse=True)
    return expanded_strings