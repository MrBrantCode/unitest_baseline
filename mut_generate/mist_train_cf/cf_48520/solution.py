"""
QUESTION:
Write a function `pattern_match_order(strings, pattern)` that filters an input list of strings `strings`. Each filtered string must contain a given sequence of patterns `patterns` in the same order, start with a given `prefix`, end with a given `suffix`, and must not contain any repeating characters. 

The function takes two parameters: `strings` which is a list of strings and `pattern` which is a tuple containing a list of patterns `patterns`, a prefix `prefix`, and a suffix `suffix`. It returns a list of strings that meet the specified conditions.
"""

from typing import List, Tuple

def pattern_match_order(strings: List[str], pattern: Tuple[List[str], str, str]) -> List[str]:
    patterns, prefix, suffix = pattern
    filtered = []

    for s in strings:
        if not (s.startswith(prefix) and s.endswith(suffix)):
            continue

        if len(s) != len(set(s)):
            continue

        indices = []
        for p in patterns:
            try:
                indices.append(s.index(p))
            except ValueError:
                break
        else:  
            if indices == sorted(indices):  
                filtered.append(s)
    return filtered