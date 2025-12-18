"""
QUESTION:
Write a function `sum_ascii` that takes a string as input and returns the sum of the ASCII values of each character in the string. Then, use this function as part of a sorting key to sort a list of names in ascending order based on the sum of the ASCII values of each character in the name. If two names have the same sum of ASCII values, sort them based on the length of the name in descending order. If the lengths of two names are also the same, sort them in lexicographical order.
"""

def sum_ascii(name):
    """
    Calculate the sum of ASCII values of each character in the name.

    Args:
    name (str): The input name.

    Returns:
    int: The sum of ASCII values of each character in the name.
    """
    return sum(ord(char) for char in name)