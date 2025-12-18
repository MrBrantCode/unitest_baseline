"""
QUESTION:
Write a function `combinationSum` that takes an array of integers `arr` and an integer `target` as input, and returns all unique combinations of exactly three elements from `arr` that sum up to `target`. The elements in each combination must be in non-decreasing order. The function should not contain any duplicate combinations. If there are duplicate elements in `arr`, the function should only consider each unique combination once.
"""

def combinationSum(arr, target):
    arr.sort()
    result = []
    def findCombinations(arr, target, start, comb):
        if target == 0 and len(comb) == 3:
            result.append(comb[:])
            return
        if target == 0:
            return
        if start >= len(arr):
            return

        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:
                continue
            comb.append(arr[i])
            findCombinations(arr, target - arr[i], i + 1, comb)
            comb.pop()
    findCombinations(arr, target, 0, [])
    return result