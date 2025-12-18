"""
QUESTION:
Create a function named `group_pairs` that takes an array of integers as input and returns a list of pairs of integers, with each pair in descending order. The function should ignore the last element if the array has an odd number of elements and the pairs should be in descending order based on the first element of the pair. Implement the solution using recursion.
"""

def group_pairs(arr):
    if len(arr) % 2 == 1:
        arr.pop()
    pairs = []
    for i in range(0, len(arr), 2):
        pair = (max(arr[i], arr[i+1]), min(arr[i], arr[i+1]))
        pairs.append(pair)
    pairs.sort(reverse=True)
    return pairs