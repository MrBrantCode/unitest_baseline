"""
QUESTION:
Write a function `closest_integer` that finds the closest integer to a given number `n` in a list `l` of integers in ascending order. If there are multiple integers with the same closest distance to `n`, return the one that appears last in the list.

The function should take two parameters: `l` (a list of integers in ascending order with a length between 2 and 10^5) and `n` (an integer between -10^9 and 10^9), and return the closest integer to `n` in the list `l`.
"""

from typing import List

def closest_integer(l: List[int], n: int) -> int:
    if n <= l[0]:
        return l[0]
    elif n >= l[-1]:
        return l[-1]
    else:
        left, right = 0, len(l) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if l[mid] == n:
                return n
            elif l[mid] < n:
                left = mid
            else:
                right = mid
        if l[right] - n <= n - l[left]:
            return l[right]
        else:
            return l[left]