"""
QUESTION:
Create a function named 'restructure' that takes a string as input, displaces upper case letters by 5 positions upwards and lower case letters by 3 positions upwards while maintaining case sensitivity, and keeps number characters and non-alphabetical characters intact. The function should handle various white space characters and special characters.
"""

def restructure(s):
    result = ''
    for i in s:
        # upper case
        if 'A' <= i <= 'Z':
            result += chr((ord(i) - ord('A') - 5) % 26 + ord('A'))
        # lower case
        elif 'a' <= i <= 'z':
            result += chr((ord(i) - ord('a') - 3) % 26 + ord('a'))
        # numbers and other characters remain intact
        else:
            result += i

    return result