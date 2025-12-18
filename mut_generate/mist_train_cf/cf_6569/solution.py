"""
QUESTION:
Implement a function named `group_pairs` that takes an array of integers as input. The function should group the elements into pairs, sort each pair in descending order, and return the pairs. If the array has an odd number of elements, the last element should be ignored. Use recursion in the implementation.
"""

def group_pairs(arr):
    if len(arr) % 2 == 1:
        arr.pop()
    pairs = []
    for i in range(0, len(arr), 2):
        pair = (arr[i], arr[i+1])
        pairs.append(pair)
    pairs.sort(reverse=True)
    return pairs