"""
QUESTION:
Implement the `find_equal_value_pair()` function, which takes a list of alphanumeric strings as input and returns a tuple containing the first pair of strings found whose values are equal based on the sum of their ASCII values. If no such pair exists, the function should return `None`. The function should be optimized for efficiency and should not assume any specific ordering of the input strings.
"""

def find_equal_value_pair(strings):
    """
    Returns a tuple containing the first pair of strings found whose values are equal based on the sum of their ASCII values.
    If no such pair exists, returns None.

    Args:
        strings (list): A list of alphanumeric strings.

    Returns:
        tuple or None: A tuple containing the first pair of strings with equal ASCII sum, or None if no pair exists.
    """
    ascii_sum = {}
    for string in strings:
        ascii_sum_for_string = sum(ord(char) for char in string)
        if ascii_sum_for_string in ascii_sum:
            return (ascii_sum[ascii_sum_for_string], string)
        ascii_sum[ascii_sum_for_string] = string
    return None