"""
QUESTION:
Write a function `check_arith_progression` that takes an array of integers as input. The function should return the common difference if the array forms a strictly ascending arithmetic progression, otherwise it should return `None`. The array should have at least two elements.
"""

def check_arith_progression(arr):
    if len(arr) < 2 or arr[1] <= arr[0]:
        return None
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return None
    return diff