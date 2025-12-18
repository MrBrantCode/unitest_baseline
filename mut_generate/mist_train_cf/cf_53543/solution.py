"""
QUESTION:
Write a function `get_sorted_modes` that takes a list of integers as input and returns a list of modes in ascending order. In cases of multiple modes, prioritize the mode with the highest weight, where the weight is the product of the mode and its frequency. If there is a tie, sort by the mode itself in ascending order. If the input list is empty, return `None`. The function should be optimized to handle large lists with up to 10,000,000 elements efficiently in terms of time and space complexity.
"""

from collections import Counter

def get_sorted_modes(lst):
    if not lst:
        return None
        
    count = Counter(lst)
    max_freq = max(count.values())

    modes = [(k, v) for k, v in count.items() if v == max_freq]
    modes.sort(key=lambda x: (-x[0]*x[1], x[0]))
    return [mode for mode, _ in modes]