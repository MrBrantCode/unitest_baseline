"""
QUESTION:
Write a function named `reverse_deque` that takes a deque `d` as input and reverses its elements without directly using any built-in reverse function. The function should use only the fundamental operations provided by the deque data structure.
"""

from collections import deque

def reverse_deque(d):
    if len(d) == 0:
        return d
    for _ in range(len(d) - 1):
        popped_element = d.pop()
        d.appendleft(popped_element)
    return d