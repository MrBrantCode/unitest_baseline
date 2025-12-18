"""
QUESTION:
Create a function called `split_string` that takes a string and a delimiter as arguments. It should return a list containing the string split by the delimiter, removing any leading or trailing whitespace from each split element. The function should handle consecutive delimiters, delimiters at the beginning or end of the string, and cases where the input string is empty or the delimiter is not found in the string. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def split_string(s, delimiter):
    """
    Splits a string by a delimiter and removes any leading or trailing whitespace from each split element.

    Args:
    s (str): The input string to be split.
    delimiter (str): The delimiter to split the string by.

    Returns:
    list: A list of split elements with leading/trailing whitespace removed.
    """
    if not s or delimiter not in s:
        return []
    
    result = []
    start = 0
    length = len(s)
    
    for i in range(length):
        if s[i] == delimiter:
            if start != i:
                result.append(s[start:i].strip())
            start = i + 1
    
    if start != length:
        result.append(s[start:].strip())
    
    return result