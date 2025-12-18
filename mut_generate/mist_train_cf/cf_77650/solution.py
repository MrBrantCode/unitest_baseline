"""
QUESTION:
Design a function named vowels_count that accepts a string as input and returns the count of vowels in the string. The function should consider 'a', 'e', 'i', 'o', 'u' as vowels, and 'y' as a vowel only when it is at the end of the string. The function should be case-insensitive and able to handle unique characters.
"""

def vowels_count(s):
    """Returns the count of vowels in the string.
    The function considers 'a', 'e', 'i', 'o', 'u' as vowels, and 'y' as a vowel only when it is at the end of the string.
    The function is case-insensitive and able to handle unique characters.

    Parameters:
    s (str): The input string.

    Returns:
    int: The count of vowels in the string.
    """
    vowels = 'aeiou'
    s = s.lower()
    count = 0
    for i in s:
        if i in vowels:
            count+=1
    if s and s[-1] == 'y':  # Check if string is not empty before checking the last character
        count+=1
    return count