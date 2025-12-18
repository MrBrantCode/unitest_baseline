"""
QUESTION:
Find the kth smallest element in an array of integers. The function name is `find_kth_smallest` and it takes two parameters: `arr` (the array of integers) and `k` (the index of the desired smallest element). The size of the array is not fixed, but the array is guaranteed to contain at least `k` elements. The function must solve the problem in O(n) time complexity, using only a constant amount of extra space, and without modifying the original array or creating a new array. Additionally, the function must not use any sorting algorithms or built-in functions.
"""

def find_kth_smallest(arr, k):
    if k > len(arr):
        return None

    pivot = arr[len(arr) // 2]  # Choosing the pivot element as the middle element of the array
    left = [num for num in arr if num < pivot]  # Elements smaller than the pivot
    right = [num for num in arr if num > pivot]  # Elements greater than the pivot
    pivot_count = len(arr) - len(left) - len(right)  # Number of elements equal to the pivot

    if k <= len(left):
        return find_kth_smallest(left, k)
    elif k <= len(left) + pivot_count:
        return pivot
    else:
        return find_kth_smallest(right, k - len(left) - pivot_count)