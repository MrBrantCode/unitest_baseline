"""
QUESTION:
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

def find_odd_occurrence(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num