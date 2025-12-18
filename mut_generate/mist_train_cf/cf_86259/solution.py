"""
QUESTION:
Write a function `generate_output(str1, str2)` that takes two strings `str1` and `str2` of equal length as input, where the length is between 1 and 1000 inclusive and contains only lowercase alphabets. The function should return a string containing alternate characters from each string without any repeated characters, and the output string should be sorted in ascending order.
"""

def generate_output(str1, str2):
    output = ""
    i, j = 0, 0

    while i < len(str1) and j < len(str2):
        char1, char2 = str1[i], str2[j]
        if char1 not in output:
            output += char1
        if char2 not in output:
            output += char2
        i += 1
        j += 1

    # Add remaining characters from str1 or str2
    while i < len(str1):
        char1 = str1[i]
        if char1 not in output:
            output += char1
        i += 1

    while j < len(str2):
        char2 = str2[j]
        if char2 not in output:
            output += char2
        j += 1

    # Sort the output string in ascending order
    output = ''.join(sorted(output))

    return output