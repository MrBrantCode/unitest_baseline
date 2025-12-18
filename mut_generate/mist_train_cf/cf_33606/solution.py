"""
QUESTION:
Implement two functions, `extractLabelInfo` and `hitState`, to parse and extract relevant information from the given input strings. 

- The `extractLabelInfo` function should take a string in the format `s0 -> s1 [label="h(0) / _"];` and return a formatted output string in the format `missState(s0, 0) == s1`.
- The `hitState` function should take a string in the format `hitState(s0, 0) == s1` and return a formatted output string in the format `hitState(s0, 0) == s1`.

The functions should handle the given input and produce the expected output based on the provided patterns, returning "Invalid input format" if the input does not match the specified formats.
"""

import re

def extractLabelInfo(input_str):
    match = re.match(r's(\d+) -> s(\d+) \[label="h\((\d+)\) / _"\];', input_str)
    if match:
        return f"missState(s{match.group(1)}, {match.group(3)}) == s{match.group(2)}"
    else:
        return "Invalid input format"

def hitState(input_str):
    match = re.match(r'hitState\(s(\d+), (\d+)\) == s(\d+)', input_str)
    if match:
        return f"hitState(s{match.group(1)}, {match.group(2)}) == s{match.group(3)}"
    else:
        return "Invalid input format"