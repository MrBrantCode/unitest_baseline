"""
QUESTION:
Write a function named `move_two_balls` that takes an array of integers as input and returns `True` if it's possible to obtain a sorted array by performing the following operations: 
right shift operation any number of times and swap exactly two elements up to two times, 
with the restriction that the resulting array must have an even number of elements smaller than the first element. Return `True` for an empty array.
"""

def move_two_balls(arr):
    if not arr:
        return True

    n = len(arr)
    inversions = 0
    small_elements = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1

            if arr[0] > arr[j]:
                small_elements += 1

    if small_elements % 2 == 0 and (inversions == 0 or inversions == 1 or inversions == 2):
        return True
    else:
        return False