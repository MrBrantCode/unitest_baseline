"""
QUESTION:
Write a function `move_three_balls(arr)` that takes an array of integers as input. 

The function should return `True` if it is possible to obtain a non-decreasingly sorted array by performing the following operations: 

- Swapping exactly two elements in the array up to three times.
- Ensuring that the number of elements smaller than the first item in the updated array is odd.
- Ensuring that all even-valued elements in the array are located at even-indexed positions (0-based).

The function should return `False` otherwise. If the provided array is empty, return `True`.
"""

def move_three_balls(arr):
    if len(arr) == 0:
        return True
    
    swaps = [0]*len(arr)
    temp = arr.copy()
    temp.sort()
    for i in range(len(arr)):
        if arr[i] != temp[i]:
            swaps[i] = 1

    if sum(swaps) > 6:
        return False
    
    for i in range(0, len(arr), 2):
        if arr[i] % 2 != 0:
            for j in range(1, len(arr), 2):
               if arr[j] % 2 == 0:
                   arr[i], arr[j] = arr[j], arr[i]
                   break

    odd_count = len([x for x in arr if x < arr[0]])
    if odd_count % 2 == 0:
        for i in range(1, len(arr)):
            if arr[i] > arr[0]:
                arr[0], arr[i] = arr[i], arr[0]
                break

    return arr == sorted(arr)