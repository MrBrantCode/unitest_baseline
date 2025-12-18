"""
QUESTION:
Write a function `replace_vowels` that takes a string and a character as input, and returns the string with all vowels replaced by the given character. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. The function should handle both uppercase and lowercase vowels.
"""

def replace_vowels(string, replace_char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        string = string.replace(vowel, replace_char)
    return string