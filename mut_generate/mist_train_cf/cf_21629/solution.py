"""
QUESTION:
Create a function named `get_unique_vowels` that takes a string as input and returns a list of unique vowels found in the string, excluding vowels that appear after a consonant and ignoring consecutive occurrences of the same vowel. The function should be case-insensitive and consider the standard English vowels 'a', 'e', 'i', 'o', and 'u'.
"""

def get_unique_vowels(string):
    """
    This function takes a string as input and returns a list of unique vowels found in the string.
    It excludes vowels that appear after a consonant and ignores consecutive occurrences of the same vowel.
    The function is case-insensitive and considers the standard English vowels 'a', 'e', 'i', 'o', and 'u'.

    Args:
        string (str): The input string to find unique vowels from.

    Returns:
        list: A list of unique vowels found in the string.
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    unique_vowels = []
    previous_consonant = False
    
    for char in string:
        if char.lower() in vowels:
            if not previous_consonant:
                if char.lower() not in unique_vowels:
                    unique_vowels.append(char.lower())
            previous_consonant = False
        else:
            previous_consonant = True
    
    return unique_vowels