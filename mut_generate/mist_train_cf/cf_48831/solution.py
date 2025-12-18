"""
QUESTION:
You are given an integer `length` and an array `updates` where `updates[i] = [startIdxi, endIdxi, inci]`. Write a function `getModifiedArray(length, updates)` to return an array where each element at index i is the array `arr` after applying the ith update from `updates` and the sum of all elements in `arr` after each update. The array `arr` has length `length` with all zeros initially, and the update operation increments all the elements `arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi]` by `inci`.

Constraints: `1 <= length <= 10^5` and `0 <= updates.length <= 10^4` and `0 <= startIdxi <= endIdxi < length` and `-1000 <= inci <= 1000`.
"""

def getModifiedArray(length, updates):
    arr = [0 for _ in range(length)]
    
    for update in updates:
        start, end, inc = update
        for i in range(start, end+1):
            arr[i] += inc
    
    return arr