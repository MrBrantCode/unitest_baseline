"""
QUESTION:
Write a function named `longest_common_substring` that takes two input strings and returns the longest contiguous substring common to both strings. The function should traverse the strings efficiently and compare characters to find the longest matching substring. The function should return the length of the longest common substring.
"""

def longest_common_substring(s1, s2):
    """
    This function finds the longest contiguous substring common to two input strings.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        int: The length of the longest common substring.
    """

    # Initialize variables to store the maximum length and the current length of the common substring
    max_length = 0
    current_length = 0

    # Initialize two pointers, one for each string
    i = j = 0

    # Traverse the two strings simultaneously
    while i < len(s1) and j < len(s2):
        # If the characters at the current positions match, increase the current length and move both pointers
        if s1[i] == s2[j]:
            current_length += 1
            i += 1
            j += 1
            # Update the maximum length if the current length is greater
            max_length = max(max_length, current_length)
        # If the characters do not match, reset the current length and move the pointer of the string with the smaller character
        else:
            current_length = 0
            if s1[i] < s2[j]:
                i += 1
            else:
                j += 1

    # Return the maximum length found
    return max_length