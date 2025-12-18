"""
QUESTION:
Implement the function `count_substring_occurrences(string, substring)` that finds the number of non-overlapping occurrences of a substring in a string. The function should be case-sensitive and account for leading and trailing whitespace characters. The substring must have a length between 2 and 10 characters and can contain alphanumeric characters, punctuation, and special symbols. The string can have a maximum length of 10^6 characters and can contain any printable ASCII characters. If the substring is empty or longer than the string, return -1.
"""

def count_substring_occurrences(string, substring):
    if len(substring) == 0 or len(substring) > len(string):
        return -1

    string = string.strip()

    start = end = 0
    count = 0

    while end < len(string):
        if string[end:end + len(substring)] == substring:
            count += 1
            start = end + len(substring)
            end = start
        else:
            end += 1

    return count