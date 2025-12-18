"""
QUESTION:
Write a function named `decode_string` that takes a string `s` as input. The string consists of a number followed by a character, indicating the number of times the character should be repeated. The function should return the decoded string where each character is repeated according to the preceding number. The function should have a time complexity of O(n) and constant space complexity, where n is the length of the string. It should not use any built-in string manipulation methods or regular expressions.
"""

def decode_string(s):
    result = ""
    count = 0
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            result += char * count
            count = 0
    return result