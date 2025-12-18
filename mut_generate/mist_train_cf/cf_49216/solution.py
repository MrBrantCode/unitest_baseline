"""
QUESTION:
Write a function `common_chars(str1, str2)` that calculates the total number of common characters present in both strings `str1` and `str2`. The function should return the total count of common characters. Note that the function should consider the frequency of each common character in both strings, i.e., it should not count a common character more times than it appears in either string.
"""

def common_chars(str1, str2):
    """
    Calculate the total number of common characters present in both strings.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    int: The total count of common characters.
    """
    
    # Convert strings to set to get unique characters from each string
    set1 = set(str1)
    set2 = set(str2)
    
    # Using set intersection property to get common characters
    common = list(set1 & set2)
    
    # Using sum and min function to count total number of common characters present in both string
    total = sum(min(str1.count(char), str2.count(char)) for char in common)
    
    return total