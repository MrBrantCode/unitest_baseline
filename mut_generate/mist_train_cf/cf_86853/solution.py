"""
QUESTION:
Write a function called `find_pairs` that takes an array of integers and a target integer as input. The function should return all pairs of numbers in the array that sum up to the target. The array may contain duplicate elements, but the output should not contain duplicate pairs. The function should have a time complexity of O(n) or better.
"""

def find_pairs(arr, target):
    seen = set()
    pairs = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)