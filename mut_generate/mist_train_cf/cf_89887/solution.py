"""
QUESTION:
Write a function named `remove_occurrences` that takes a string `string` and a character `letter` as input. The function should remove all occurrences of `letter` that are immediately followed by a digit from the `string` and return the resulting string with no trailing spaces, along with the count of removed occurrences.
"""

def remove_occurrences(string, letter):
    occurrences_removed = 0
    result = ""
    i = 0
    while i < len(string):
        if string[i] == letter and i < len(string) - 1 and string[i + 1].isdigit():
            occurrences_removed += 1
            i += 2
        else:
            result += string[i]
            i += 1
    result = result.rstrip()
    return result, occurrences_removed