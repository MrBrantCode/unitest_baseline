"""
QUESTION:
Write a function named "remove_consecutive_reverse" that takes a string as input, removes all consecutive characters from the string in a case-sensitive manner, and returns the non-consecutive characters in reverse order. The function should handle strings with both uppercase and lowercase letters and be implemented using recursion.
"""

def remove_consecutive_reverse(s):
    # Base case: if the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    
    # Check if the first two characters are consecutive
    if s[0] == s[1]:
        # If they are, remove the consecutive characters and call the function recursively
        return remove_consecutive_reverse(s[2:])
    else:
        # If they are not consecutive, add the first character to the reversed string
        return s[0] + remove_consecutive_reverse(s[1:])[::-1]