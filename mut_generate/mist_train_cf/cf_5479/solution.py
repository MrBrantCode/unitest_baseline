"""
QUESTION:
Write a function `print_consonants` that takes a string as input and prints each consonant in the string one at a time, excluding vowels and spaces, while ignoring uppercase and lowercase distinctions. The function should also return the total count of consonants in the string.
"""

def print_consonants(input_string):
    """
    Prints each consonant in the input string one at a time, excluding vowels and spaces,
    while ignoring uppercase and lowercase distinctions. Returns the total count of consonants.

    Args:
        input_string (str): The input string to process.

    Returns:
        int: The total count of consonants in the string.
    """
    consonant_count = 0
    for char in input_string:
        if char.lower() not in ['a', 'e', 'i', 'o', 'u'] and char != " ":
            print(char)
            consonant_count += 1
    return consonant_count