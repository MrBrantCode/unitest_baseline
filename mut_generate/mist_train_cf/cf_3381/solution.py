"""
QUESTION:
Write a function named `reverse_string_exclude_vowels_special_chars` that takes a string as input and returns the string in reverse order, excluding vowels and special characters. The solution should have a time complexity of O(n^2) and a space complexity of O(n), where n is the length of the string.
"""

def reverse_string_exclude_vowels_special_chars(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '<', '>', '.', ',', '/', '?', '|', '\\'}
    reversed_string = ""
    for char in s[::-1]:
        if char.isalpha() and char not in vowels and char not in special_chars:
            reversed_string += char
    return reversed_string