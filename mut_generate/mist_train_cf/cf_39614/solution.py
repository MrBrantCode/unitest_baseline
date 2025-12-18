"""
QUESTION:
Given a positive integer 's' representing the maximum weight that can be carried and a list of integers 'items' representing the sizes of different items, write a function `max_items(s, items)` to determine the maximum number of items that can be carried without exceeding the weight limit 's'. The function should return the maximum number of items that can be carried within the weight limit. The input list of items is not sorted, and it contains only non-negative integers.
"""

from typing import List

def max_items(s: int, items: List[int]) -> int:
    items.sort()  # Sort the items in ascending order
    total_weight = 0
    max_items_count = 0

    for item in items:
        if total_weight + item <= s:  # Check if adding the current item exceeds the weight limit
            total_weight += item
            max_items_count += 1
        else:
            break  # If adding the current item exceeds the weight limit, stop adding more items

    return max_items_count