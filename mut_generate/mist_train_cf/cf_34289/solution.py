"""
QUESTION:
Implement the `parseStr` function, which takes a string as input and returns a dictionary containing the count of each character in the string, ignoring spaces and considering 'A' and 'a' as the same character. The function should not include spaces in the output dictionary and should be case-insensitive.
"""

def parseStr(input_str):
    input_str = input_str.lower()
    char_count = {}
    for char in input_str:
        if char != ' ':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count