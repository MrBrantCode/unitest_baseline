"""
QUESTION:
Write a function `search_substrings` that performs a case-insensitive substring search in a given input string. The function should consider a substring a match only if it is surrounded by spaces or punctuation marks. It should return a dictionary with the count of occurrences for each substring in the input string. The function should be able to handle large input strings efficiently and handle non-ASCII characters in the input string and substrings. It should also allow multiple substrings to be searched for. The function should take two parameters: `input_string` and `substrings`.
"""

import re
import string

def search_substrings(input_string, substrings):
    translator = str.maketrans('', '', string.punctuation)
    input_string = input_string.translate(translator)

    input_string = input_string.lower()
    substrings = [substring.lower() for substring in substrings]

    occurrences = {substring: 0 for substring in substrings}

    pattern = r'(?<!\S)(%s)(?!\S)' % '|'.join(map(re.escape, substrings))

    for match in re.finditer(pattern, input_string):
        matched_substring = match.group(1)
        occurrences[matched_substring] += 1

    return occurrences