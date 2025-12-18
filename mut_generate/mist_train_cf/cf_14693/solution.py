"""
QUESTION:
Design a function `findMedianSortedArrays` that takes two sorted arrays `array1` and `array2` as input and returns their median. The function should have a time complexity of O(log(min(n, m))), where n and m are the sizes of the two arrays respectively. Assume the arrays are sorted in non-decreasing order.
"""

def findMedianSortedArrays(array1, array2):
    if len(array1) > len(array2):
        array1, array2 = array2, array1
        n, m = len(array2), len(array1)
    else:
        n, m = len(array1), len(array2)

    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        partition2 = (n + m + 1) // 2 - mid

        leftMax1 = float('-inf') if mid == 0 else array1[mid - 1]
        leftMax2 = float('-inf') if partition2 == 0 else array2[partition2 - 1]
        rightMin1 = float('inf') if mid == n else array1[mid]
        rightMin2 = float('inf') if partition2 == m else array2[partition2]

        if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
            if (n + m) % 2 == 1:
                return max(leftMax1, leftMax2)
            else:
                return (max(leftMax1, leftMax2) + min(rightMin1, rightMin2)) / 2
        elif leftMax1 > rightMin2:
            high = mid - 1
        else:
            low = mid + 1
    return -1