"""
QUESTION:
Create a function called `search_patterns` that takes two parameters: a string to search within and a list of regular expression patterns. The function should return a list of dictionaries containing the matched pattern, the matched substring, and its start and end indices within the string. The function should be able to handle overlapping patterns and nested patterns without performance issues.
"""

import re

def search_patterns(string, patterns):
    results = []
    for pattern in patterns:
        matches = re.finditer(pattern, string)
        for match in matches:
            start_index = match.start()
            end_index = match.end()
            results.append({
                'pattern': pattern,
                'match': match.group(),
                'start_index': start_index,
                'end_index': end_index
            })
    return results