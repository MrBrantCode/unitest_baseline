"""
QUESTION:
Write a function `find_pairs(arr, target)` that takes an array of integers and a target integer as input and returns all pairs of numbers in the array that sum up to the target. The array may contain duplicate elements, and the output should not contain duplicate pairs. The function should have a time complexity of O(n) or better.
"""

def find_pairs(arr, target):
    seen = set()
    pairs = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)
    return list(pairs)