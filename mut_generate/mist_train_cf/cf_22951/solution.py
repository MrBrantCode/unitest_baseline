"""
QUESTION:
Create a function called `compress_string` that takes a string as input and returns a string of tuples representing consecutive occurrences of each character. Each tuple should contain a character and its count, and the function should not use any built-in string manipulation or counting methods.
"""

def compress_string(s):
    compressed_string = ""
    count = 1
    for i in range(len(s)):
        if i != len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            compressed_string += "(" + s[i] + "," + str(count) + ")"
            count = 1
    return compressed_string