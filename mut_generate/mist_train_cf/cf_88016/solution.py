"""
QUESTION:
Write a function `count_vowels(text)` that counts the number of vowels in a given text, ignoring consecutive vowels and vowels followed by 'v', 'x', or 'z', but counting vowels followed by the same consonants twice consecutively. The function should be case-insensitive and return the count as an integer.
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