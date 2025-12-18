"""
QUESTION:
Write a function named count_unique_vowels that takes a list of strings as input, converts each string to lowercase, concatenates them into a single string, and returns the number of unique vowels in the resulting string. The list can contain any number of strings. The function should only consider the standard English vowels 'a', 'e', 'i', 'o', and 'u'.
"""

def count_unique_vowels(strings):
    """
    This function takes a list of strings, converts them to lowercase, 
    concatenates them, and returns the number of unique vowels.

    Args:
        strings (list): A list of strings.

    Returns:
        int: The number of unique vowels in the concatenated string.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    concatenated_string = ''.join(s.lower() for s in strings)
    unique_vowels = set(c for c in concatenated_string if c in vowels)
    return len(unique_vowels)