"""
QUESTION:
Write a function `find_most_frequent_char` that takes a string `s` as input and returns the most frequent character and its count in the string. The function should use recursion and not rely on any built-in functions or additional data structures such as dictionaries, arrays, or sets. The function should also handle empty strings and strings with multiple characters having the same highest frequency.
"""

def find_most_frequent_char(s, max_char=None, max_count=0):
    if len(s) == 0:
        return max_char, max_count

    current_char = s[0]
    count = count_occurrences(s, current_char)

    if count > max_count:
        max_char = current_char
        max_count = count

    return find_most_frequent_char(s[1:], max_char, max_count)


def count_occurrences(s, char):
    if len(s) == 0:
        return 0

    if s[0] == char:
        return 1 + count_occurrences(s[1:], char)
    else:
        return count_occurrences(s[1:], char)