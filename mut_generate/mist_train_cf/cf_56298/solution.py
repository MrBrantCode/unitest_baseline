"""
QUESTION:
Given two integer arrays of equal length `target` and `arr`, determine if it's possible to make `arr` equal to `target` by selecting any non-empty sub-array of `arr` and reversing it, or by swapping any two elements in `arr`. If it's possible, return True and the minimum number of steps required; otherwise, return False and -1.

The function name is `canBeEqual(target, arr)` where `target` and `arr` are the input arrays. The length of both arrays is between 1 and 1000 (inclusive), and each element is an integer between 1 and 1000 (inclusive).
"""

def canBeEqual(target, arr):
    if len(target) != len(arr):
        return False, -1
    if sorted(arr) == sorted(target):
        return True, 0
    freq_target = {}
    freq_arr = {}
    for i in range(len(target)):
        if target[i] not in freq_target:
            freq_target[target[i]] = 0
        freq_target[target[i]] += 1
        if arr[i] not in freq_arr:
            freq_arr[arr[i]] = 0
        freq_arr[arr[i]] += 1
    if freq_arr != freq_target:
        return False, -1
    count = 0
    for i in range(len(target)):
        if arr[i] != target[i]:
            j = arr.index(target[i])
            arr[i:(j+1)] = arr[i:(j+1)][::-1]
            count += 1
    return True, count