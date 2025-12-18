"""
QUESTION:
Create a function `contains_consecutive_vowels(word)` that takes a string as input and returns `True` if the string contains at least one pair of consecutive vowels, and `False` otherwise. Assume vowels are 'a', 'e', 'i', 'o', and 'u'.
"""

def contains_consecutive_vowels(word):
    vowels = 'aeiou'
    for i in range(len(word) - 1):  
        if word[i] in vowels and word[i+1] in vowels:  
            return True  
    return False  