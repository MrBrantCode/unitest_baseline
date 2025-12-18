"""
QUESTION:
Write a function `move_two_balls(arr)` that determines whether it's possible to rearrange the array into a non-decreasing order by performing the following operations: 
- right shift operation any number of times
- swap exactly two elements in the array up to two instances.

The array may or may not contain unique components, and it should be considered as sorted if it's empty.
"""

def move_two_balls(arr):
    if len(arr) == 0:
        return True

    even_positions = []
    odd_positions = []
    for i, n in enumerate(arr):
        if n % 2 == 0:
            even_positions.append(i)
        else:
            odd_positions.append(i)

    if len(even_positions) % 2 == 1:
        return False

    odd_swaps = 0
    even_swaps = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 != 0:
            even_swaps += 1
        elif i % 2 == 1 and arr[i] % 2 == 0:
            odd_swaps += 1

    return (even_swaps <= 2) and (odd_swaps <= 2)