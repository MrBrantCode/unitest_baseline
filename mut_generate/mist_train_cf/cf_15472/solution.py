"""
QUESTION:
Write a function named `remove_vowels` that takes a string as input and returns two values: a modified string with all vowels removed and the count of consonants in the modified string. The function should consider both lowercase and uppercase English vowels (a, e, i, o, u, A, E, I, O, U) and only count alphabetic characters as consonants.
"""

def remove_vowels(string):
    """
    Removes vowels from the input string and counts the consonants.
    
    Args:
    string (str): The input string.
    
    Returns:
    tuple: A tuple containing the modified string with vowels removed and the count of consonants.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    modified_string = ""
    consonant_count = 0
    
    for char in string:
        if char not in vowels:
            modified_string += char
            if char.isalpha():
                consonant_count += 1
    
    return modified_string, consonant_count