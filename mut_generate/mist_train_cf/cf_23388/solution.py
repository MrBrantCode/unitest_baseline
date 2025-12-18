"""
QUESTION:
Write a function called `top_three_longest_strings` that takes an array of strings as input and returns the top 3 strings with the greatest length. The input array can contain any number of strings, but the output should always be limited to the top 3 longest strings. If there are less than 3 strings in the input array, return all of them.
"""

def top_three_longest_strings(arr):
    """
    Returns the top 3 strings with the greatest length from the input array.

    Args:
        arr (list): A list of strings.

    Returns:
        list: A list of the top 3 longest strings.
    """
    return sorted(arr, key=len, reverse=True)[:3]