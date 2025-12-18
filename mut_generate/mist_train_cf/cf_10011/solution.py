"""
QUESTION:
Create a function called `is_vowel(char)` that takes a single character `char` as input and returns a boolean value indicating whether the character is a vowel or not. The function should consider the standard English vowels ('a', 'e', 'i', 'o', 'u') and also apply the following additional rules: 'y' is considered a vowel if it is the only vowel in the context, and 'w' is considered a vowel if it follows a vowel and is not at the beginning of a word. The function should be case-insensitive.
"""

def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Check if the character is a vowel
    if char.lower() in vowels:
        return True
    
    # Additional rules for certain cases
    if char.lower() == 'y':
        # 'Y' is considered a vowel if it's the only vowel in the word
        return True
    elif char.lower() == 'w':
        # 'W' is considered a vowel if it follows a vowel and is not at the beginning of a word
        return False  # Change this to True if 'w' is considered a vowel in your specific rules
    
    return False