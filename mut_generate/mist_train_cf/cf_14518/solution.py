"""
QUESTION:
Develop a function `findSmallest(arr, start, end)` that takes a list of integers `arr` and two indices `start` and `end` as input, and returns the index of the smallest element in the sublist `arr[start:end+1]`. The function should use recursion and handle duplicate values in the list efficiently.
"""

def findSmallest(arr, start, end):
    if start == end:
        return start

    mid = (start + end) // 2
    leftSmallest = findSmallest(arr, start, mid)
    rightSmallest = findSmallest(arr, mid + 1, end)

    if arr[leftSmallest] <= arr[rightSmallest]:
        return leftSmallest
    else:
        return rightSmallest