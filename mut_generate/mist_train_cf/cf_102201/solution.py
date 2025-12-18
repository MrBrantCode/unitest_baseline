"""
QUESTION:
Write a function called `count_letters` that takes a string as input and returns a dictionary where the keys are the letters in the string and the values are their corresponding counts. The function should be case-insensitive, meaning it should treat 'a' and 'A' as the same letter. The function should only count letters (a-z or A-Z) and ignore any other characters.
"""

def count_letters(string_name):
    """
    This function takes a string as input and returns a dictionary where the keys are the letters in the string 
    and the values are their corresponding counts. The function is case-insensitive and only counts letters (a-z or A-Z).

    Args:
        string_name (str): The input string.

    Returns:
        dict: A dictionary where the keys are the letters in the string and the values are their corresponding counts.
    """
    letter_counts = {}
    for char in string_name.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts