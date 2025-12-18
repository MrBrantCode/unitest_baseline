"""
QUESTION:
Write a function named `organize_strings` that takes an array of strings as input and returns a new array with all strings that start with a vowel (A, E, I, O, U) placed at the beginning, followed by the remaining strings. The function should ignore case when checking for vowels.
"""

def organize_strings(strings):
    """
    Reorganize an array of strings to place all strings that start with a vowel at the beginning.
    
    Args:
        strings (list): The input list of strings.
    
    Returns:
        list: The reorganized list of strings.
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowel_strings = [string for string in strings if string[0].upper() in vowels]
    remaining_strings = [string for string in strings if string[0].upper() not in vowels]
    
    return vowel_strings + remaining_strings