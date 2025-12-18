"""
QUESTION:
Write a function called `remove_occurrences` that takes a string and a letter as input. The function should remove all occurrences of the given letter that are immediately followed by a digit from the string, remove any trailing spaces from the resulting string, and return the resulting string along with the number of occurrences of the given letter that were removed. The function should not modify the original string.
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