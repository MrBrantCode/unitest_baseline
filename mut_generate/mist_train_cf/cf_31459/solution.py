"""
QUESTION:
Create a function `extract_substrings` that takes in a string `input_string` and a list of patterns `pattern_list`. The function should use regular expressions to match each pattern in the `pattern_list` against the `input_string` and return a list of matched substrings. If a pattern does not match any substring in the `input_string`, the function should include `None` in the output list for that pattern.
"""

import re
from typing import List, Optional

def extract_substrings(input_string: str, pattern_list: List[str]) -> List[Optional[str]]:
    matched_substrings = []
    for pattern in pattern_list:
        match = re.search(pattern, input_string)
        if match:
            matched_substrings.append(match.group(0))
        else:
            matched_substrings.append(None)
    return matched_substrings