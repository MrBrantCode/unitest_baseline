"""
QUESTION:
Create a function named `check_anagrams` that takes two strings as input. The function should check if the two input strings are anagrams of each other, ignoring non-alphanumeric characters and considering uppercase and lowercase letters as the same. The function should return True if the strings are anagrams and False otherwise.
"""

def check_anagrams(str1, str2):
    """
    This function checks if two input strings are anagrams of each other.
    
    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    
    # Remove spaces and punctuation marks, and convert to lowercase
    str1 = "".join(e for e in str1 if e.isalnum()).lower()
    str2 = "".join(e for e in str2 if e.isalnum()).lower()

    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)