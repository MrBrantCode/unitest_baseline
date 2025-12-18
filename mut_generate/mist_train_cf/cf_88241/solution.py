"""
QUESTION:
Write a function called `find_last_vowel()` that returns the last vowel character of a given string using recursion, without using the built-in function `len()`.
"""

def find_last_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Base case: if string is empty, return None
    if not string:
        return None
    
    # Recursive case: if the last character is a vowel, return it
    if string[-1].lower() in vowels:
        return string[-1]
    
    # Recursive case: if the last character is not a vowel, call the function again with the substring excluding the last character
    return find_last_vowel(string[:-1])