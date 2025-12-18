"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the string in reverse order, excluding any vowels and special characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def reverse_string(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ':', ';', '<', '>', '?', ',', '.', '/', '|', '\\'}
    reversed_string = ""
    
    for char in reversed(string):
        if char.isalpha() and char not in vowels and char not in special_chars:
            reversed_string += char
    
    return reversed_string