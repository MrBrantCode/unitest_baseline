"""
QUESTION:
Write a function `reverse_string_exclude_vowels_special_chars` that takes a string as input, reverses it, excludes any vowels and special characters, and returns the result. The function should have a time complexity of O(n^2) and a space complexity of O(n), where n is the length of the string.
"""

def reverse_string_exclude_vowels_special_chars(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '<', '>', '.', ',', '/', '?', '|', '\\'}
    reversed_string = ""
    for char in string[::-1]:
        if char.isalpha() and char not in vowels and char not in special_chars:
            reversed_string += char
    return reversed_string