"""
QUESTION:
Create a function named `count_vowels` that takes a string as input and returns the number of vowels (both lowercase and uppercase) in the string, excluding whitespace characters and without using the `len()` function. The function should be case-insensitive, treating 'a' and 'A' as the same character.
"""

def count_vowels(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count