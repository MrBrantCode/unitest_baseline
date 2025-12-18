"""
QUESTION:
Given a sorted or unsorted array of integers and an integer target, write a function `combinationSum` that finds all unique combinations of exactly three elements from the array that sum up to the target. The elements in each combination must be in non-decreasing order. The function should not contain duplicate combinations.
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