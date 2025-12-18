"""
QUESTION:
Create a function `vowel_checker` that accepts a list of words and returns `True` if any word contains a vowel ('a', 'e', 'i', 'o', 'u') in its second, fourth, or sixth letter position, and `False` otherwise. The function should be case-insensitive.
"""

def vowel_checker(word_list):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for word in word_list:
        for i, letter in enumerate(word.lower(), start=1):
            if i in [2, 4, 6] and letter in vowels:
                return True
    return False