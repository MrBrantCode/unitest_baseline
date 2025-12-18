"""
QUESTION:
Write a function `find_max_consecutive_vowels` that takes a string as input and returns a tuple containing the maximum number of consecutive vowels and the substring with the maximum number of consecutive vowels. The function should be case-insensitive and consider only the standard English vowels 'a', 'e', 'i', 'o', and 'u'.
"""

def find_max_consecutive_vowels(string):
    """
    This function finds the maximum number of consecutive vowels and the corresponding substring in a given string.

    Args:
    string (str): The input string.

    Returns:
    tuple: A tuple containing the maximum number of consecutive vowels and the substring with the maximum number of consecutive vowels.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_count = 0
    current_count = 0
    max_substring = ""
    current_substring = ""

    for char in string:
        if char.lower() in vowels:
            current_count += 1
            current_substring += char
        else:
            if current_count > max_count:
                max_count = current_count
                max_substring = current_substring
            current_count = 0
            current_substring = ""

    # Check if the last substring has more consecutive vowels than the previous maximum
    if current_count > max_count:
        max_count = current_count
        max_substring = current_substring

    return max_count, max_substring