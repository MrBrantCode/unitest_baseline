"""
QUESTION:
Write a function 'combineStrings' that takes two strings and a delimiter as input, and returns the combined string with the delimiter between them. The function should handle the cases where one or both of the input strings are empty, and the delimiter can be a single character or a string. The time complexity of the function should be O(n), where n is the total length of the input strings.
"""

def combineStrings(string1, string2, delimiter):
    """
    Combine two strings with a delimiter.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.
        delimiter (str): The delimiter to use.

    Returns:
        str: The combined string.
    """
    if not string1 and not string2:  
        return delimiter
    elif not string1:  
        return delimiter + string2
    elif not string2:  
        return string1 + delimiter
    else:  
        return string1 + delimiter + string2