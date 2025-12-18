"""
QUESTION:
Write a function `check_vowels` that takes a string `input_string` as input and returns `True` if the string contains all the vowels (a, e, i, o, u) at least once, ignoring case, and returns `False` otherwise. If the string contains the letter 'y', the function should return `False`.
"""

def check_vowels(input_string):
    vowels = 'aeiou'
    found_vowels = set()
    for char in input_string.lower(): 
        if char in vowels:
            found_vowels.add(char)
        elif char == 'y':
            return False
    return len(found_vowels) == len(vowels)