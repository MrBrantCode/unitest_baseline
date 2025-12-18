"""
QUESTION:
Create a function named `merge_lists` that takes two lists of integers, `list1` and `list2`, and returns a merged list without any duplicates. The elements from `list2` should appear first in the merged list, ordered by their frequency in `list1` (in descending order). If two elements have the same frequency, they should be ordered by their original order in `list2`. The remaining elements from `list1` should be appended to the end of the merged list, in ascending order. The time complexity of the function should be O(n log n).
"""

from typing import List
from collections import Counter

def merge_lists(list1: List[int], list2: List[int]) -> List[int]:
    """ From two lists of integers, merge them based on element frequency from first to second list, excluding duplicates. """
    # Create a frequency count dictionary for list1 elements
    counts = Counter(list1)

    # Create sets to remove duplicates from both lists
    set_list1 = set(list1)
    set_list2 = set(list2)

    # Sort list2 by frequency of elements in list1, then by their order of appearance in list2
    list2_sorted = sorted(set_list2, key = lambda x: (-counts[x], list2.index(x)))

    # Return the sorted list2 followed by any remaining unique elements from list1
    return list2_sorted + sorted(set_list1 - set_list2)