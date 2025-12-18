"""
QUESTION:
Write a function named `replace_vowels` that takes two parameters: `string` and `replace_char`. Replace all vowels (both lowercase and uppercase) in the input `string` with the given `replace_char` and return the modified string. The solution should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1). The function should assume that the given `replace_char` will always be a single character.
"""

def replace_vowels(string, replace_char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        string = string.replace(vowel, replace_char)
    return string