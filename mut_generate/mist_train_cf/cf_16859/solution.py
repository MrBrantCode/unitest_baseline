"""
QUESTION:
Write a function `sort_string` that takes a string as input, removes all non-alphabetic characters, sorts the remaining alphabets in descending order based on their ASCII values, and returns the sorted string along with the count of each unique alphabet in the original string.
"""

def sort_string(s):
    """
    This function takes a string as input, removes all non-alphabetic characters, 
    sorts the remaining alphabets in descending order based on their ASCII values, 
    and returns the sorted string along with the count of each unique alphabet.

    Args:
    s (str): The input string.

    Returns:
    tuple: A tuple containing the sorted string and a dictionary with the count of each unique alphabet.
    """
    # Remove all characters except for alphabets
    new_string = ''.join(c for c in s if c.isalpha())

    # Sort the alphabets in descending order based on their ASCII values
    sorted_string = ''.join(sorted(new_string, reverse=True))

    # Count the occurrences of each unique alphabet
    count_dict = {}
    for c in s:
        if c.isalpha():
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1

    return sorted_string, count_dict