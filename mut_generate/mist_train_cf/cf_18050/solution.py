"""
QUESTION:
Create a function `find_non_repeating_vowels` that takes a string as input and returns a list of non-repeating vowels. A non-repeating vowel is a vowel that appears only once in the string, excluding any vowels that appear more than once consecutively. The function should be case-insensitive, meaning it treats 'a' and 'A' as the same vowel.
"""

def find_non_repeating_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    non_repeating_vowels = []
    i = 0
    
    while i < len(string):
        if string[i].lower() in vowels:
            if i+1 < len(string) and string[i].lower() == string[i+1].lower():
                i += 1
            else:
                non_repeating_vowels.append(string[i].lower())
        i += 1
    
    return non_repeating_vowels