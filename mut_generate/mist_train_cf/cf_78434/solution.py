"""
QUESTION:
Create a function named `merge_strings` that takes two strings of unequal length as input and returns a new string with characters of both strings alternating. If the strings are of unequal length, the function should append the remaining characters of the longer string. If both strings are numeric, the function should return an error message. The function should not assume the order or length of the input strings.
"""

def merge_strings(s1, s2):
    if s1.isdigit() and s2.isdigit():
        return "Error: Both strings are numeric."

    short_length = min(len(s1), len(s2))
    result = ""

    for i in range(short_length):
        result += s1[i] + s2[i]

    if len(s1) > len(s2):
        result += s1[short_length:]
    else:
        result += s2[short_length:]

    return result