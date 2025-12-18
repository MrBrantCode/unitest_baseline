"""
QUESTION:
Design a function `count_occurrences_and_find_specific_endings` that takes in a list of strings `data` and two optional parameters `start_pattern` (default 'Foo') and `end_pattern` (default '123'). The function should use regular expressions to efficiently search through the dataset, count all occurrences of words starting with `start_pattern` followed by any alphanumeric characters, and identify words that also end with `end_pattern`. The function should return a Counter object containing the count of each matching word and a list of words that end with `end_pattern`.
"""

import re
from collections import Counter

def count_occurrences_and_find_specific_endings(data, start_pattern='Foo', end_pattern='123'):
    pattern = re.compile(r'\b{}[a-zA-Z0-9]*?\b'.format(start_pattern))
    specific_endings = re.compile(r'\b{}[a-zA-Z0-9]*?{}\b'.format(start_pattern, end_pattern))

    all_matches = Counter()
    specific_end = []

    for line in data:
        line_matches = pattern.findall(line)
        all_matches.update(line_matches)

        for word in line_matches:
            if specific_endings.fullmatch(word):
                specific_end.append(word)

    return all_matches, specific_end