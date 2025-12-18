"""
QUESTION:
Write a method `replace_odd_occurrences` for a string class that takes in two parameters, `substring` and `replace_with`. If the `substring` appears an odd number of times in the string, replace all occurrences of the `substring` with the `replace_with` characters. If the `substring` appears an even number of times or does not appear at all, return the original string unchanged. The method should return a string.
"""

def replace_odd_occurrences(string, substring, replace_with):
    """
    Replaces all occurrences of a substring with replace_with if the substring appears an odd number of times in the string.

    Args:
        string (str): The input string.
        substring (str): The substring to search for.
        replace_with (str): The string to replace the substring with.

    Returns:
        str: The modified string if the substring appears an odd number of times, otherwise the original string.
    """
    count = string.count(substring)
    if count % 2 != 0:
        return string.replace(substring, replace_with)
    return string