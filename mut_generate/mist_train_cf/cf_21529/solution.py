"""
QUESTION:
Create a function `split_and_reverse_string` that takes a string as input. The function should split the string into individual words, excluding any words that start with a vowel (a, e, i, o, u), ignore punctuation marks and special characters, and return the list of words in reverse order. The function should be case-insensitive.
"""

def split_and_reverse_string(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = s.lower().split()
    result = []
    
    for word in words:
        # Remove punctuation marks and special characters
        word = ''.join(e for e in word if e.isalnum())
        
        # Exclude words that start with a vowel
        if word and word[0] not in vowels:
            result.append(word)
    
    return result[::-1]