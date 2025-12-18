"""
QUESTION:
Given a sequence of non-negative integers, find a trio of numbers a, b, and c that satisfy the following conditions: a + b = 4, c = 5, and the sum of c and twice the cumulative absolute difference between each pair of consecutive elements in the sequence equals the total sum of all elements. Implement the function `find_abc(arr)` to yield a tuple of integers (a, b, c). If multiple solutions are possible, return any one of them. If no solution can be found, return (-1, -1, -1).
"""

from typing import List, Tuple

def find_abc(arr: List[int]) -> Tuple[int, int, int]:
    a_b_combinations = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
    sum_arr = sum(arr)

    for a, b in a_b_combinations:
        cumulative_diff = sum([abs(arr[i] - arr[i-1]) for i in range(1, len(arr))])
        if (2 * cumulative_diff) + 5 == sum_arr:
            return a, b, 5

    return -1, -1, -1