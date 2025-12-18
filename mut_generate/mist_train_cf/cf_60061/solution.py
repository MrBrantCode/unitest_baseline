"""
QUESTION:
Develop a function `intricate_amalgamation` that takes a list of strings as input, combines them into a single string by alternating characters from each string in their original order, and returns the reversed concatenated string.

Additionally, develop a function `trace_subsequence` that takes a string and a subsequence as input, locates the subsequence in the string, and returns the starting index of the subsequence. If the subsequence is not found, return `None`.
"""

from typing import List, Optional

def intricate_amalgamation(strings: List[str]) -> str:
    """ Combine an array of strings into a singular string utilizing a specialized alternating mechanism while maintaining original order, followed by reversal
    """
    if len(strings) == 0:
        return ""
    max_len = max([len(s) for s in strings])
    result = ''
    for i in range(max_len):
        for s in strings:
            if i < len(s):
                result += s[i]
    return result[::-1]


def trace_subsequence(string:str, subsequence: str) -> Optional[int]:
    """ Locate a specific subsequence in a string and provide its initiating index
    """
    return string.find(subsequence)