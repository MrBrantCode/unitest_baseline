"""
QUESTION:
Write a function `find_invalid_number(preamble, sequence)` that takes in two parameters: `preamble`, a list of distinct integers representing the initial preamble of numbers, and `sequence`, a list of integers representing the sequence of additional numbers. The function should return the first number in the sequence that does not have the property of being the sum of two distinct numbers from the preamble. The length of the preamble is fixed and greater than 1, and all numbers in the sequence are distinct.
"""

from typing import List

def find_invalid_number(preamble: List[int], sequence: List[int]) -> int:
    for x in sequence:
        valid = False
        for i, a in enumerate(preamble[:-1]):
            for b in preamble[i+1:]:
                if a + b == x:
                    valid = True
        if not valid:
            return x
        preamble = preamble[1:] + [x]