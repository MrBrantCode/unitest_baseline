"""
QUESTION:
Create a function called `remove_vowels` that takes a string as input and returns a new string with all vowels (both lowercase and uppercase) removed. The function should achieve this in O(n) time complexity and constant space complexity.
"""

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    new_string = ""
    for char in s:
        if char not in vowels:
            new_string += char
    return new_string