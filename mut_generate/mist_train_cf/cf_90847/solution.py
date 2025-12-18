"""
QUESTION:
Write a function called `remove_vowels` that takes a string `s` as input and returns a new string with all the vowels removed. The function should have a time complexity of O(n) and use constant space complexity.
"""

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in s:
        if char not in vowels:
            new_string += char
    return new_string