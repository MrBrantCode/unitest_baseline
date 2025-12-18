"""
QUESTION:
Create a function `char_to_num_sum` that takes a string as input and returns the sum of the values of all the characters in the string based on the following mapping: A = 1, B = 2, C = 3, a = 1, b = 2, c = 3. The function should ignore any characters not in the mapping.
"""

def char_to_num_sum(s):
    """
    Calculate the sum of the values of all characters in a string based on the mapping:
    A = 1, B = 2, C = 3, a = 1, b = 2, c = 3. Non-mapped characters are ignored.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the values of the characters in the string.
    """
    char_to_num = {'A': 1, 'B': 2, 'C': 3, 'a': 1, 'b': 2, 'c': 3}
    return sum(char_to_num.get(char, 0) for char in s)