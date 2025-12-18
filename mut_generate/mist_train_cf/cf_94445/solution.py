"""
QUESTION:
Implement a function `count_substring_occurrences` that takes two parameters: `string` and `substring`. The function should find the number of non-overlapping occurrences of the `substring` in the `string`. The function should be case-sensitive and should account for leading and trailing whitespace characters in the `string`. The `substring` must have a length between 3 and 20 characters and can contain alphanumeric characters, punctuation, and special symbols. If the `substring` is empty or longer than the `string`, the function should return -1.
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