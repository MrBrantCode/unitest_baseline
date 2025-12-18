"""
QUESTION:
Create a function called `split_sort_join_reverse` that takes a string `s` and an integer `n` as parameters, where `n` is greater than the length of `s`. The function should split `s` into substrings of length `n`, sort the resulting list in descending order, join the elements using a hyphen (`-`) delimiter, and return the reversed final string.
"""

def split_sort_join_reverse(s, n):
    """
    Splits a string into substrings of length n, sorts the substrings in descending order, 
    joins them using a hyphen delimiter, and returns the reversed final string.

    Parameters:
    s (str): The input string
    n (int): The length of the substrings (greater than the length of s)

    Returns:
    str: The reversed final string
    """
    split_list = [s[i:i+n] for i in range(0, len(s), n)]
    split_list.sort(reverse=True)
    joined_string = "-".join(split_list)
    return joined_string[::-1]