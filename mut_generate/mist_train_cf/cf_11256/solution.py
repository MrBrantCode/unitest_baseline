"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the string in reverse order while excluding any vowels and special characters. The function should consider both lowercase and uppercase vowels.
"""

def reverse_string(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/', '`', '~']
    
    reversed_string = s[::-1]  # Reverse the string
    
    final_string = ''
    for char in reversed_string:
        if char.isalpha() and char not in vowels:
            final_string += char
    
    return final_string