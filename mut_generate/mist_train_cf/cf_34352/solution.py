"""
QUESTION:
Implement a function `largest_number(a)` that takes an array of non-negative integers `a` and returns the largest number that can be formed by concatenating the elements of the array in any order. The function should return the result as a string.

The input array `a` is not empty and contains only non-negative integers.
"""

from typing import List

def largest_number(a: List[int]) -> str:
    # Custom comparator function to compare two numbers when concatenated
    def compare(x, y):
        return int(str(x) + str(y)) - int(str(y) + str(x))

    # Sort the array using the custom comparator
    a.sort(key=lambda x: str(x), reverse=True)

    # Join the sorted array to form the largest number
    return str(int(''.join(map(str, a))))