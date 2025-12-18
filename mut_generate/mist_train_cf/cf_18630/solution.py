"""
QUESTION:
Create a function `are_anagrams` that takes two string parameters, `string1` and `string2`, and returns a boolean value indicating whether the two input strings are anagrams. The function should be case-insensitive, ignore whitespace and punctuation marks, handle Unicode characters, and have a time complexity of O(n log n), where n is the length of the longer input string. The function should be able to handle input strings of length up to 10^6.
"""

def are_anagrams(string1, string2):
    """
    This function checks if two input strings are anagrams of each other.
    
    The function is case-insensitive, ignores whitespace and punctuation marks, 
    handles Unicode characters, and has a time complexity of O(n log n), where n 
    is the length of the longer input string. It can handle input strings of length 
    up to 10^6.

    Parameters:
    string1 (str): The first input string.
    string2 (str): The second input string.

    Returns:
    bool: True if the input strings are anagrams, False otherwise.
    """

    # Convert both strings to lower case and remove whitespace and punctuation
    s1 = ''.join(e for e in string1 if e.isalnum()).lower()
    s2 = ''.join(e for e in string2 if e.isalnum()).lower()

    # If the sorted forms of the two strings are equal, they are anagrams
    return sorted(s1) == sorted(s2)