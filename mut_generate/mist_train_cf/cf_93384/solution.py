"""
QUESTION:
Write a function `remove_vowels_reverse` that takes a string as input, removes all the vowels from it, and returns the resulting string in reverse order. The function should consider both lowercase and uppercase vowels.
"""

def remove_vowels_reverse(string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result[::-1]