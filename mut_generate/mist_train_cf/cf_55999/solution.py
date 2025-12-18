"""
QUESTION:
Write a function called `search_pattern` that takes two parameters: `string` and `pattern`. The function should use a regular expression to search for the specified pattern within the given string. It should return a list of dictionaries, where each dictionary contains the matched substring, its starting index, and its ending index within the original string.
"""

import re

def search_pattern(string, pattern):
    matches = [m for m in re.finditer(pattern, string)]
    results = []
    for match in matches:
        results.append({
            'substring': match.group(0),
            'start': match.start(),
            'end': match.end()
        })
    return results