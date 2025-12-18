"""
QUESTION:
Create a function named `check_vowels` that takes a string as input and returns a boolean indicating whether the string contains all the vowels ('a', 'e', 'i', 'o', 'u') in alphabetical order, without any repeated vowels, and has a length of 100 characters or less.
"""

def check_vowels(string):
    vowels = 'aeiou'
    if len(string) > 100:
        return False

    vowels_found = []
    for char in string:
        if char.lower() in vowels:
            if char.lower() in vowels_found:
                return False
            if len(vowels_found) > 0 and vowels.index(char.lower()) < vowels.index(vowels_found[-1]):
                return False
            vowels_found.append(char.lower())
    
    return len(vowels_found) == len(vowels)