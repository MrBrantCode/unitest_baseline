"""
QUESTION:
Write a function named `find_second_occurrence` that takes two parameters, `string` and `substring`, and returns the index of the second occurrence of `substring` in `string`. The function should be case-sensitive and handle strings containing non-alphanumeric characters, multiple occurrences of the substring, Unicode characters, and edge cases such as empty strings or substrings. The function should not use built-in string or substring searching methods.
"""

def find_second_occurrence(string, substring):
    if not string or not substring:
        return -1

    length = len(string)
    sub_length = len(substring)
    count = 0
    i = 0

    while i < length:
        if string[i:i+sub_length] == substring:
            count += 1
            if count == 2:
                return i
            i += sub_length
        else:
            i += 1

    return -1