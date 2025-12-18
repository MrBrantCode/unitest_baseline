"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the reverse of the string. The function should handle Unicode characters and special characters correctly, preserving their original positions. Implement the function using only iterative techniques, without using any built-in functions or methods that directly reverse a string or recursion. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_string(input_string):
    characters = list(input_string)
    start = 0
    end = len(characters) - 1

    while start < end:
        if ord(characters[start]) >= 0xD800 and ord(characters[start]) <= 0xDBFF:
            characters[start], characters[start + 1] = characters[start + 1], characters[start]
            start += 2
        else:
            characters[start], characters[end] = characters[end], characters[start]
            start += 1
            end -= 1

    return ''.join(characters)