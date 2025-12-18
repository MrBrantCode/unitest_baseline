"""
QUESTION:
Create a function named `vowels_count` that accepts a string representing a word containing alpha numerical characters, special characters, and non-ASCII characters. The function should return the total count of vowels, mystery vowels, and uppercase 'Y'. Vowels are defined as 'a', 'e', 'i', 'o', and 'u', and a mystery vowel is any vowel immediately followed by a special character. The function should handle mixed case, ignore case for vowels other than 'Y', and only consider 'Y' as a vowel when it is uppercase.
"""

def vowels_count(s):
    """
    Extend a function named vowels_count that accepts a string that could include alpha numerical characters, 
    special characters and non-ascii characters. The function should return the total count of vowels, 
    mystery vowels, and uppercase 'Y'.

    For this function, vowels should follow the standard definition of 'a', 'e', 'i', 'o', and 'u'. A mystery
    vowel is any vowel immediately followed by a special character.

    """
    vowels = "aeiou"
    special = string.punctuation
    count = 0
    s_lower = s.lower()
    for v in vowels:
        count += s_lower.count(v)
        for sp in special:
            count += s_lower.count(v + sp)
    count += s.count('Y')
    return count