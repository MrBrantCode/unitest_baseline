"""
QUESTION:
Implement the `merge_sort` function to sort an array in descending order using the merge sort algorithm without recursion. The array may contain duplicate elements. You must use iteration and a stack data structure. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr

    stack = []
    for i in range(n):
        stack.append([arr[i]])

    while len(stack) > 1:
        pair1 = stack.pop()
        pair2 = stack.pop()

        merged = merge(pair1, pair2)
        stack.append(merged)

    return stack[0]

def merge(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] >= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged