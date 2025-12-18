"""
QUESTION:
Write a function `find_longest_string(strings)` that takes a list of strings as input and returns the longest string that only contains alphabetic characters. If the input list is empty or all strings contain numbers or special characters, the function should return `None`. If multiple strings have the same maximum length, the function should return the first occurrence of the longest string. The function should have a time complexity of O(n), where n is the total number of characters in all the strings combined.
"""

def find_longest_string(strings):
    """
    This function finds the longest string that only contains alphabetic characters in a given list of strings.
    
    Args:
    strings (list): A list of strings.
    
    Returns:
    str or None: The longest string that only contains alphabetic characters, or None if no such string exists.
    """
    
    if not strings:
        return None
    
    longest = ""
    for string in strings:
        if not string.isalpha():
            continue
        
        if len(string) > len(longest):
            longest = string
    
    return longest if longest else None