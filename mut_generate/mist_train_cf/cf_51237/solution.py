"""
QUESTION:
Create a function named `vowels_count` that takes a string as input and returns the count of vowels present in the string. The function should consider 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase) as vowels and 'y' (both lowercase and uppercase) as a vowel only when it appears at the end of the string. The function should be case-insensitive and handle strings containing unconventional characters.
"""

import re

VOWELS = set('aeiouAEIOU')

def vowels_count(s):
    """
    This function takes a string as input and returns the count of vowels present in the string.
    The function considers 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase) as vowels 
    and 'y' (both lowercase and uppercase) as a vowel only when it appears at the end of the string.

    Parameters:
    s (str): The input string to count vowels in.

    Returns:
    int: The count of vowels in the string.
    """
    # Use regular expression to replace all characters except alphabets and 'y' at the end
    s = re.sub(r'[^a-zA-ZyY]|[^yY]y', '', s)
    
    # Use a generator expression within the sum function to count the vowels
    count = sum(1 for c in s if c in VOWELS or (c.lower() == 'y' and s[-1].lower() == 'y'))
    
    return count