"""
QUESTION:
Write a function `replace_vowels` that replaces all vowels in a given string with underscores, preserving the original case of each vowel character, and removes all consecutive duplicate vowels.
"""

def replace_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''
    prev_vowel = False
    
    for char in string:
        if char in vowels:
            if prev_vowel:
                result += ''
            else:
                result += '_'
                prev_vowel = True
        else:
            result += char
            prev_vowel = False
    
    return result