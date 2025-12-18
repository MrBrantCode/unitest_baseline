"""
QUESTION:
Write a function `find_max_subset(text: str)` that determines the most extensive contiguous subset of characters within the provided text string, counts the number of occurrences of this subset, and provides the starting and ending indices of each occurrence in the string. The function should be case sensitive and consider special characters and spaces as valid characters.

The function should return a tuple containing the most extensive contiguous subset, the number of occurrences of this subset, and a list of tuples where each tuple contains the start and end indices of each occurrence of the subset. The solution should aim for a time complexity better than O(n²), where n is the length of the string, and avoid using Python's in-built string count functions.
"""

from collections import defaultdict
from typing import List, Tuple

def find_max_subset(text: str) -> Tuple[str, int, List[Tuple[int, int]]]:
    n = len(text)
    count_dict = defaultdict(list)
    max_len = 0
    max_str = ""

    for i in range(n):
        temp_str = ""
        for j in range(i, n):
            temp_str += text[j]
            count_dict[temp_str].append((i, j))
            if len(temp_str) > max_len:
                max_len = len(temp_str)
                max_str = temp_str

    max_subset = max_str
    occurrence = len(count_dict[max_str])
    ranges = count_dict[max_str]
    return max_subset, occurrence, ranges