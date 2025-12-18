"""
QUESTION:
Write a function `find_second_occurrence(string, substring)` that finds the index of the second occurrence of `substring` in `string`. The search is case-sensitive and should not use built-in string searching methods like `find()` or `index()`. The function should handle strings with non-alphanumeric characters, multiple occurrences of the substring, Unicode characters, and edge cases like empty strings or substrings. If the substring occurs less than twice, the function should return -1.
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