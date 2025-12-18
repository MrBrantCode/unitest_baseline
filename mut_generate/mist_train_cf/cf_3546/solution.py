"""
QUESTION:
Create a function `count_vowels(text)` that counts the number of vowels in a given text. A vowel is only counted if it is not followed by a specific consonant ('v', 'x', 'z') and not part of a consecutive sequence of vowels. If a vowel is followed by a specific consonant twice consecutively, it should be counted as one occurrence. The function should be case-insensitive.
"""

def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    specific_consonants = ['v', 'x', 'z']
    count = 0
    text = text.lower()
    length = len(text)
    
    i = 0
    while i < length:
        char = text[i]
        
        if char in vowels:
            if i+1 < length and text[i+1] in specific_consonants:
                i += 1
            elif i+1 < length and text[i+1] in vowels:
                i += 1
            else:
                count += 1
        i += 1
    
    return count