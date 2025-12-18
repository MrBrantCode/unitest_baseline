"""
QUESTION:
Write a function `unique_substrings(s)` that calculates the total number of substrings without repeating characters in a given string `s`. The function should use a sliding window approach and return the total count of unique substrings. The input string `s` will only contain lowercase letters.
"""

def unique_substrings(s):
    """
    Calculate the total number of substrings without repeating characters in a given string.
    
    Parameters:
    s (str): The input string containing only lowercase letters.
    
    Returns:
    int: The total count of unique substrings.
    """
    num_of_substrings = 0
    visited = set()
    left = right = 0
    while right < len(s):
        if s[right] not in visited:
            visited.add(s[right])
            right += 1
            num_of_substrings += len(visited)
        else:
            visited.remove(s[left])
            left += 1
    return num_of_substrings