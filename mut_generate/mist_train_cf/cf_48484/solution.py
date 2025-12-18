"""
QUESTION:
Find the least positive integer missing from a given array of integers in non-ascending or non-descending order, with a computational complexity of O(n) and a space complexity of O(1). The function should be named `findMissing` and take two parameters: the input array `arr` and its size `size`. Note that the input array may contain duplicate values and that the solution should modify the input array in place.
"""

def findMissing(arr, size):
    j = 0
    for i in range(size):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    for i in range(size):
        if abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0 and i >= j:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    for i in range(size):
        if arr[i] > 0 and i >= j:
            return i + 1 - j
    return size + 1 - j