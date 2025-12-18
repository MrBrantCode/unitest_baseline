"""
QUESTION:
Write a function `generate_output(str1, str2)` that takes two strings `str1` and `str2` of equal length as input and returns a string containing alternate characters from each string, with no repeated characters, in ascending order. The strings `str1` and `str2` contain only lowercase alphabets and their lengths are between 1 and 1000, inclusive.
"""

def entance(str1, str2):
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