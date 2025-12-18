"""
QUESTION:
Implement a function named `search_substrings` that performs a case-insensitive substring search. The function should take two parameters: `input_string` and `substrings`, where `input_string` is the string to search in, and `substrings` is a list of substrings to search for. 

The function should return a dictionary where the keys are the substrings and the values are their corresponding counts in the input string. A substring is considered a match only if it is surrounded by spaces or punctuation marks. The function should handle large input strings efficiently and support non-ASCII characters in the input string and substrings.
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