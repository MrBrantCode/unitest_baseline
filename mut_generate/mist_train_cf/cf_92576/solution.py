"""
QUESTION:
Write a function `find_pairs` that takes an array of integers `arr` and an integer `value` as input. The function should return a list of all distinct pairs of integers in `arr` whose sum is equal to `value`. The function should be able to handle negative integers and zeros in the array.
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