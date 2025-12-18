"""
QUESTION:
Implement a function `process_lines` that takes a list of strings `lines`, a regular expression pattern `pattern`, and an integer `limit`. The function should return a list of integers representing the 0-indexed starting positions of lines that match the `pattern` up to the specified `limit`. The function should stop processing once `limit` number of matches is reached.
"""

import re

def find_line_positions(lines, pattern, limit):
    matched_positions = []
    pattern = re.compile(pattern)

    for i, line in enumerate(lines):
        if pattern.match(line):
            matched_positions.append(i)
            if len(matched_positions) == limit:
                break

    return matched_positions