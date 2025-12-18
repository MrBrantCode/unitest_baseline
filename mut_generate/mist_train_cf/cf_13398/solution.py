"""
QUESTION:
Write a function `longest_common_substring` that finds the longest common substring between two input strings. The longest common substring must be at least three characters long and is case-sensitive. Both input strings must be alphanumeric and have a minimum length of five characters each.
"""

def longest_common_substring(s1, s2):
    """
    Finds the longest common substring between two input strings.
    
    Args:
    s1 (str): The first input string.
    s2 (str): The second input string.
    
    Returns:
    str: The longest common substring between s1 and s2. If no common substring is found, returns an empty string.
    """
    
    # Check if both strings are alphanumeric and have a minimum length of five characters each
    if not (s1.isalnum() and s2.isalnum() and len(s1) >= 5 and len(s2) >= 5):
        return ""
    
    # Initialize variables to store the longest common substring and its length
    longest_substring = ""
    max_length = 0
    
    # Iterate over the characters in the first string
    for i in range(len(s1)):
        # Iterate over the characters in the second string
        for j in range(len(s2)):
            # Initialize variables to store the current common substring and its length
            current_substring = ""
            k = 0
            
            # Compare characters in both strings starting from the current positions
            while i + k < len(s1) and j + k < len(s2) and s1[i + k] == s2[j + k]:
                current_substring += s1[i + k]
                k += 1
            
            # Update the longest common substring if the current one is longer
            if len(current_substring) > max_length and len(current_substring) >= 3:
                longest_substring = current_substring
                max_length = len(current_substring)
    
    return longest_substring