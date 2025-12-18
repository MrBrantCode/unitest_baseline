"""
QUESTION:
Implement a function `process_deque(d)` that takes a deque `d` as input and returns a list of integers representing the values of `max` after each operation. The function should replicate the behavior described below:

- If the deque `d` is empty, return an empty list.
- Initialize a variable `max` to the value of the first element in the deque `d` and remove it from the deque.
- While the deque `d` is not empty, perform the following steps:
  - If the first element of the deque `d` is less than or equal to `max`, remove it from the left end of the deque and update the value of `max` to the removed element.
  - If the last element of the deque `d` is less than or equal to `max`, remove it from the right end of the deque and update the value of `max` to the removed element.
  - If neither of the above conditions is met, break the loop and return the list of integers representing the values of `max` after each operation.
"""

from collections import deque

def process_deque(d):
    if not d:
        return []

    max_values = []
    max_val = d.popleft()
    max_values.append(max_val)

    while d:
        if d[0] <= max_val:
            max_val = d.popleft()
            max_values.append(max_val)
        elif d[-1] <= max_val:
            max_val = d.pop()
            max_values.append(max_val)
        else:
            break

    return max_values