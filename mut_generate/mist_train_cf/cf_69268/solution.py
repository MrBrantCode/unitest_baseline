"""
QUESTION:
Write a function `common_substring(strings, k)` that takes a list of strings `strings` and an integer `k` as input, and returns the longest shared subsequence string in the list that appears at least `k` times. If no such string exists or the list is empty, return `None`. In case of a tie, return the first earliest occurring string. The function should have a time complexity of at least O(n^2).
"""

from typing import List, Optional
from collections import defaultdict

def longest_common_subsequence(strings: List[str], k: int) -> Optional[str]:
    """
    This function finds the longest shared subsequence string in a list of strings 
    that appears at least k times. If no such string exists or the list is empty, 
    it returns None. In case of a tie, it returns the first earliest occurring string.

    Args:
        strings (List[str]): A list of strings.
        k (int): The minimum frequency of the subsequence.

    Returns:
        Optional[str]: The longest shared subsequence string or None.
    """

    n = len(strings)
    common = defaultdict(int)
    longest_str = None
    max_length = -1

    if n == 0 or k < 1:
        return None

    else:
        for string in strings:
            checked = set()

            for i in range(len(string)):
                for j in range(i + 1, len(string) + 1):
                    substring = string[i:j]

                    if substring not in checked:
                        checked.add(substring)
                        common[substring] += 1

                        if common[substring] >= k:
                            if j - i > max_length:
                                longest_str = substring
                                max_length = len(substring)

    return longest_str