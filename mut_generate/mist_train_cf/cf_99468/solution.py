"""
QUESTION:
Write a function `reverse_string` that takes a string as input and reverses it in-place using only the letters of the original string. The function should not use any pre-built methods or libraries for reversing the string. It should only modify the letters in the original string, keeping non-alphabetic characters in their original positions.
"""

def reverse_string(string):
    letters = [char for char in string if char.isalpha()]
    reversed_letters = letters[::-1]
    index = 0
    result = list(string)
    for i, char in enumerate(string):
        if char.isalpha():
            result[i] = reversed_letters[index]
            index += 1
    return ''.join(result)