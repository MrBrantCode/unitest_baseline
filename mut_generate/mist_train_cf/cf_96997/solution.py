"""
QUESTION:
Write a function `decode_string(encoded_string)` that takes a string as input and returns the decoded string. The input string may contain lowercase and uppercase alphabets, digits, and special characters. Each digit in the string represents the repeat count of the character immediately following it. If a character is not preceded by a digit, it is assumed to have a repeat count of 1. The function should have a time complexity of O(n), where n is the length of the string, and a constant space complexity.
"""

def decode_string(encoded_string):
    decoded_string = ''
    repeat_count = 0
    for char in encoded_string:
        if char.isdigit():
            repeat_count = repeat_count * 10 + int(char)
        else:
            if repeat_count == 0:
                decoded_string += char
            else:
                decoded_string += char * repeat_count
                repeat_count = 0
    return decoded_string