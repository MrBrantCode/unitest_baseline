"""
QUESTION:
Write a function called `convert_to_uppercase_and_count` that takes a string as input and returns a tuple. The tuple should contain the input string with all lowercase letters converted to uppercase and the count of lowercase letters converted. The function should not use the built-in `upper()` function. The function should return the original characters unchanged if they are not lowercase letters.
"""

def convert_to_uppercase_and_count(s):
    count = 0
    uppercase_s = ''

    for char in s:
        if 97 <= ord(char) <= 122:  # ASCII values for 'a' to 'z'
            uppercase_s += chr(ord(char) - 32)  # ASCII values for 'A' to 'Z'
            count += 1
        else:
            uppercase_s += char

    return uppercase_s, count