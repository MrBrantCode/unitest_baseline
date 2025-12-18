"""
QUESTION:
Create a function `count_vowels` that takes a string as input and returns the number of vowels in the string until a whitespace is encountered. The function should not use any built-in string manipulation functions and should be case-insensitive. The vowels are 'a', 'e', 'i', 'o', and 'u'.
"""

def entrance(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for char in string:
        if char == ' ':
            break
        elif char.lower() in vowels:
            count += 1

    return count