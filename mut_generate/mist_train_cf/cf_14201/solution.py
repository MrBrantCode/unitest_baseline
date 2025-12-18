"""
QUESTION:
Write a function `longest_vowel_start` that takes an array of strings as input and returns the longest string that starts with a vowel. The function should consider both lowercase and uppercase vowels. If there are multiple strings of the same maximum length that start with a vowel, it can return any one of them.
"""

def longest_vowel_start(strings):
    """
    Returns the longest string that starts with a vowel from the given array of strings.
    
    Parameters:
    strings (list): A list of strings.
    
    Returns:
    str: The longest string that starts with a vowel.
    """
    vowels = 'aeiouAEIOU'
    longest = ''
    for string in strings:
        if string[0] in vowels and len(string) > len(longest):
            longest = string
    return longest