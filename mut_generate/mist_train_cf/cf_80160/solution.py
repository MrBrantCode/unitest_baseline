"""
QUESTION:
Write a function `consonants_average` that takes a string as input and returns the average count of consonants present in the string. Consonants are all alphabets excluding 'a', 'e', 'i', 'o', 'u', and '.' when it appears in the middle of the word. The function should ignore the case of consonants and handle unusual symbols in the word. If the input string is empty, the function should return 0.
"""

def consonants_average(s):
    """Return the average count of consonants present in the string.
    'Consonants' refers to all alphabets excluding 'a', 'e','i','o','u', and '.' ONLY
    when it appears in the middle of the word. Ignore the case of consonants and handle 
    unusual symbols in the word.

    """
    consonants = [char for char in s.lower() if char.isalpha() and char not in {'a', 'e', 'i', 'o', 'u'}]
    return len(consonants) / len(s) if s else 0