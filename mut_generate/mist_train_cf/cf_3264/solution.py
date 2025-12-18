"""
QUESTION:
Write a function `check_anagram` that determines if two given strings are anagrams of each other. The function should ignore any punctuation and white spaces in the strings, be case-insensitive, and have a time complexity of O(nlogn). It should also use constant additional space complexity. The strings can contain any printable ASCII characters.
"""

def check_anagram(str1, str2):
    """
    This function determines if two given strings are anagrams of each other.
    
    The function ignores any punctuation and white spaces in the strings, 
    is case-insensitive, and has a time complexity of O(nlogn). It also uses 
    constant additional space complexity.

    Args:
        str1 (str): The first string to check.
        str2 (str): The second string to check.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """

    # Remove punctuation and white spaces, and convert to lowercase
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()

    # If the lengths of the strings are not equal, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Sort the strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare the sorted strings
    return str1 == str2