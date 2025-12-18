"""
QUESTION:
Complete the function 'longest_common_substring' to return the longest common substring from a list of strings. The function should return an empty string if no common substring exists among the list of strings or if the input list is empty. The function should be able to handle any number of input strings and substrings of any length.
"""

from typing import List

def longest_common_substring(strings: List[str]) -> str:
    def helper(str1: str, str2: str) -> str:
        m = [[0] * (1 + len(str2)) for _ in range(1 + len(str1))]
        longest, x_longest = 0, 0
        for x in range(1, 1 + len(str1)):
            for y in range(1, 1 + len(str2)):
                if str1[x - 1] == str2[y - 1]:
                    m[x][y] = m[x - 1][y - 1] + 1
                    if m[x][y] > longest:
                        longest = m[x][y]
                        x_longest = x
                else:
                    m[x][y] = 0
        return str1[x_longest - longest: x_longest]

    if not strings:
        return ""
    
    common_str = strings[0]
    for s in strings[1:]:
        common_str = helper(common_str, s)
        if not common_str:
            return ""
    
    return common_str