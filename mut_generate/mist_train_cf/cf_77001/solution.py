"""
QUESTION:
Implement the function 'longest_common_subsequence' to return the longest common subsequence from a list of strings. Unlike substrings, subsequences are not required to occupy consecutive positions within the original strings. If no common subsequence exists among the list of strings or if the list is empty, return None.

The function takes a list of strings as input and returns a string representing the longest common subsequence, or None if no common subsequence exists. The time and space complexity of the solution should be optimized.
"""

from typing import List, Optional

def longest_common_subsequence(strings: List[str]) -> Optional[str]:
    """
    This function returns the longest common subsequence from a list of strings.
    
    Args:
    strings (List[str]): A list of strings.
    
    Returns:
    Optional[str]: The longest common subsequence, or None if no common subsequence exists.
    """
    
    # If the list is empty, return None
    if not strings:
        return None
    
    # Sort the strings by length in ascending order
    strings.sort(key=len)
    
    # Initialize the shortest string
    shortest_str = strings[0]
    
    # Initialize the longest common subsequence
    lcs = ""
    
    # Iterate over the length of the shortest string
    for length in range(len(shortest_str), 0, -1):
        # Iterate over the starting index of the subsequence
        for i in range(len(shortest_str) - length + 1):
            # Get the subsequence
            subsequence = shortest_str[i:i+length]
            
            # Check if the subsequence is common to all strings
            if all(subsequence in string for string in strings):
                # Update the longest common subsequence
                lcs = subsequence
                break
        
        # If a common subsequence is found, break the loop
        if lcs:
            break
    
    return lcs