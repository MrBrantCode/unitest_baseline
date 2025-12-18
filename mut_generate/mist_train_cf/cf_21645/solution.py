"""
QUESTION:
Write a function called `reverse_string` that takes a string as input, removes any leading or trailing whitespace characters, and returns the reverse of the resulting string. The function should handle strings with special characters and maintain their original positions in the reversed string. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in string manipulation functions or data structures.
"""

def reverse_string(input_string):
    input_string = input_string.strip()
    characters = list(input_string)
    left, right = 0, len(characters) - 1
    while left < right:
        characters[left], characters[right] = characters[right], characters[left]
        left += 1
        right -= 1
    return ''.join(characters)