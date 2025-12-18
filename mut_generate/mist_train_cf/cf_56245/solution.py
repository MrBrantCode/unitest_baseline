"""
QUESTION:
Write a function `eliminate_excess(arr)` that takes an array of integers as input and returns a new array with all integers that occur more than three times in the original array removed, while preserving the original order of elements. The function should have a time complexity of O(n).
"""

def eliminate_excess(arr):
    cnt = {}
    result = []

    for num in arr:
        if num not in cnt:
            cnt[num] = 1
            result.append(num)
        elif cnt[num] < 3:
            cnt[num] += 1
            result.append(num)

    return result