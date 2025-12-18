"""
QUESTION:
Implement a function named `count_substring_occurrences` that takes two parameters, `string` and `substring`, and returns the number of non-overlapping occurrences of `substring` in `string`. The function must be case-sensitive, ignore leading and trailing whitespace in `substring`, and only match substrings with lengths between 3 and 20 characters. Return -1 if `substring` is empty or longer than `string`.
"""

import re

def count_substring_occurrences(string, substring):
    if len(substring) == 0 or len(substring) > len(string):
        return -1

    # Trim leading and trailing whitespace characters
    substring = substring.strip()

    # Validate that the substring length is between 3 and 20 characters
    if len(substring) < 3 or len(substring) > 20:
        return -1

    # Escape special characters in the substring for regex matching
    substring = re.escape(substring)

    # Construct the regex pattern for matching non-overlapping occurrences of the substring
    pattern = r'(?<!\S)' + substring + r'(?!\S)'

    # Use regex to find all non-overlapping occurrences of the substring in the string
    occurrences = re.findall(pattern, string)

    # Return the count of occurrences
    return len(occurrences)