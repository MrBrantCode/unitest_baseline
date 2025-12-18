"""
QUESTION:
Write a function `reverse_string_exclude_vowels` that takes a string as input and returns the reversed string excluding any vowels (both lowercase and uppercase) and spaces, while maintaining the original casing of the characters.
"""

def reverse_string_exclude_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']
    return ''.join([char for char in input_string[::-1] if char not in vowels])