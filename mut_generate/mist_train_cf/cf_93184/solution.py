"""
QUESTION:
Write a function `find_second_occurrence(string, substring)` that returns the index of the second occurrence of `substring` in `string`. The function should be case-sensitive and have a time complexity of O(n), where n is the length of `string`, and a space complexity of O(1). If `substring` does not occur at least twice in `string`, the function should return -1.
"""

def find_second_occurrence(string, substring):
    """
    Returns the index of the second occurrence of substring in string.
    
    Args:
        string (str): The string to search in.
        substring (str): The substring to search for.
    
    Returns:
        int: The index of the second occurrence of substring in string. 
             Returns -1 if substring does not occur at least twice in string.
    """
    first_occurrence = string.find(substring)
    if first_occurrence == -1:
        return -1
    second_occurrence = string.find(substring, first_occurrence + 1)
    return second_occurrence