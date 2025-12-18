"""
QUESTION:
Write a function `count_pattern_occurrences` that takes two parameters, `pattern` and `string`, and returns the number of times the `pattern` occurs in the `string`. The function should be case-sensitive and should count overlapping occurrences. The length of the `pattern` can be any value greater than 0.
"""

def count_pattern_occurrences(pattern, string):
    """
    Returns the number of times the pattern occurs in the string.
    
    The function is case-sensitive and counts overlapping occurrences.
    
    Parameters:
    pattern (str): The pattern to search for.
    string (str): The string to search in.
    
    Returns:
    int: The number of occurrences of the pattern in the string.
    """
    count = 0
    pattern_length = len(pattern)
    string_length = len(string)

    for i in range(string_length - pattern_length + 1):
        if string[i:i+pattern_length] == pattern:
            count += 1

    return count