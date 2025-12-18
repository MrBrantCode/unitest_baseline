"""
QUESTION:
Write a function `find_pairs(arr, value)` that takes an array of integers and a target integer value as input, and returns a list of all distinct pairs of integers in the array whose sum is equal to the given value. The function should handle negative integers and zeros in the array.
"""

def find_pairs(arr, value):
    pairs = []
    seen = set()
    for num in arr:
        complement = value - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs