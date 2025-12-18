"""
QUESTION:
Write a function `rotate_deque` that takes a list of items representing a deque and a binary string as input. The function should cyclically rotate the deque according to the provided binary string, rotating to the right for each '1' and to the left for each '0'. The function should return the rotated deque as a list.

Restrictions: The binary string will always contain the same number of elements as the deque.
"""

def rotate_deque(deque_items, binary_string):
    from collections import deque
    d = deque(deque_items)
    for i in binary_string:
        if i == '1':
            d.rotate(1)
        else:
            d.rotate(-1)
    return list(d)