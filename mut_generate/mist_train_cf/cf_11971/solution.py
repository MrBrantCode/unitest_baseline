"""
QUESTION:
Write a function called `reverse_concat_without_vowels` that takes two strings as input, concatenates them, removes all vowels from the concatenated string, and returns the resulting string reversed. Vowels include both lowercase and uppercase letters.
"""

def reverse_concat_without_vowels(string1, string2):
    concatenated_string = string1 + string2
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in concatenated_string:
        if char not in vowels:
            result += char
    
    return result[::-1]