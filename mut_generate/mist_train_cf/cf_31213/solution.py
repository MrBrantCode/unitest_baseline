"""
QUESTION:
Write a function `rearrange_max_to_front` that takes a list of integers `A` as input. The function should rearrange the elements in the list such that the maximum absolute value element is moved to the front of the list. If multiple elements have the same maximum absolute value, the one with the lower index should be moved to the front. The function should not change the order of other elements in the list.
"""

from typing import List

def rearrange_max_to_front(A: List[int]) -> List[int]:
    a_max = A[0]
    i_max = 0
    for i, item in enumerate(A):
        if abs(item) > abs(a_max) or (abs(item) == abs(a_max) and i < i_max):
            i_max, a_max = i, item
    A.insert(0, A.pop(i_max))
    return A