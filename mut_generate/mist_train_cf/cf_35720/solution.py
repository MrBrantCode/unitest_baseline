"""
QUESTION:
Implement a function mergeSort that sorts an array using the merge sort algorithm and returns the number of inversions in the array. An inversion occurs when a larger element appears before a smaller element in the array. The function should take an array and the left and right indices of the subarray to be sorted as input. 

The mergeSort function should be used to implement the countInversions function, which takes an array and its length as input and returns the number of inversions in the array. 

Restrictions: The mergeSort function should have a time complexity of O(n log n) and should use the merge sort algorithm to sort the array and count the inversions.
"""

def merge_sort(arr, left, right):
    if right > left:
        mid = left + (right - left) // 2
        inversions = 0
        inversions += merge_sort(arr, left, mid)
        inversions += merge_sort(arr, mid + 1, right)
        inversions += merge(arr, left, mid, right)
        return inversions
    return 0

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [arr[left + i] for i in range(n1)]
    R = [arr[mid + 1 + j] for j in range(n2)]

    inversions = 0
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inversions += n1 - i  # Count inversions
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return inversions