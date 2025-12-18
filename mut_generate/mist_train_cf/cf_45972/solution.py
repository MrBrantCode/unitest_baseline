"""
QUESTION:
Write a function called `findDisappearedNumbers` that takes a list of integers `nums` as input and returns a dictionary where the keys are all the integers in the range `[1, n]` that do not appear in `nums` and the values are their frequencies in `nums`. The function should not use any extra space beyond the input `nums` and the output dictionary, and it should have a runtime of `O(n)`. The length of `nums` is `n`, and each integer in `nums` is in the range `[1, n]`.
"""

def findDisappearedNumbers(nums):
    from collections import Counter
    count = Counter(nums)
    n = len(nums)
    return {i: count.get(i, 0) for i in range(1, n + 1) if i not in count}