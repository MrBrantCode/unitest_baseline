"""
QUESTION:
Create a function named `vowel_starting_strings` that takes a list of strings as input. The function should return a set of strings that start with a vowel (both lowercase and uppercase), and the set should be sorted in descending order based on the length of each string. The function should not take any other parameters besides the list of strings.
"""

def vowel_starting_strings(strings):
    """
    Returns a set of strings that start with a vowel (both lowercase and uppercase), 
    sorted in descending order based on the length of each string.

    Args:
    strings (list): A list of strings.

    Returns:
    set: A set of strings that start with a vowel, sorted in descending order by length.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return set(string for string in strings if string[0].lower() in vowels)