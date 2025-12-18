"""
QUESTION:
Create a function `filter_array` that takes a list of integers `numbers` and an integer `threshold` as input, and returns two lists. The function should exclude even numbers, imaginary integers, and elements that occur more than the specified `threshold` times. The first returned list should contain the remaining elements in their original order, and the second list should contain the discarded elements in their original order.
"""

from typing import List, Tuple

def filter_array(numbers: List[int], threshold: int) -> Tuple[List[int], List[int]]:
    frequency = {}
    remain = []
    discard = []

    for num in numbers:
        if isinstance(num, int) and num % 2 != 0:
            freq = frequency.get(num, 0) + 1
            if freq <= threshold:
                remain.append(num)
                frequency[num] = freq
            elif freq > threshold:
                discard.append(num)
        else:
            discard.append(num)
    return remain, discard