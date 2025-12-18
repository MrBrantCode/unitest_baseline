"""
QUESTION:
Write a function `character_count` that takes a string as input and returns a dictionary where the keys are the unique characters in the string and the values are their corresponding counts. The function should handle any type of character, including spaces and punctuation.
"""

def character_count(s):
    """
    This function takes a string as input and returns a dictionary where the keys are the unique characters in the string and the values are their corresponding counts.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary where the keys are the unique characters in the string and the values are their corresponding counts.
    """
    character_count_dict = {}
    for char in s:
        character_count_dict[char] = character_count_dict.get(char, 0) + 1
    return character_count_dict