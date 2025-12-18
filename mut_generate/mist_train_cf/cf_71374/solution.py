"""
QUESTION:
Implement a function `increment_and_shift` that takes a list of numbers as input. The function should modify the list such that each even-indexed element is incremented by the value of the next odd-indexed element, unless it is the last element, in which case it is incremented by 10. The odd-indexed elements remain unchanged.
"""

def increment_and_shift(arr):
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            arr[i] += arr[i + 1]
        else:
            arr[i] += 10
    return arr