"""
QUESTION:
Implement a function `count_substring_occurrences(string, substring)` that finds the number of non-overlapping occurrences of `substring` in `string`. The function should be case-sensitive, account for leading and trailing whitespace characters in `string`, and return -1 if `substring` is empty or longer than `string`. The length of `substring` should be between 2 and 10 characters, and it can contain alphanumeric characters, punctuation, and special symbols. The length of `string` can be up to 10^6 characters, and it can contain any printable ASCII characters.
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