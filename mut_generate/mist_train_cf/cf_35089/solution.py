"""
QUESTION:
Write a function `count_inversions(arr)` that takes an array of distinct integers `arr` and returns the number of inversions in the array, where an inversion occurs when there are two indices `i` and `j` such that `i < j` and `arr[i] > arr[j]`. The array can have up to 10^5 elements.
"""

def count_inversions(arr):
    def merge(arr, temp, left, mid, right):
        i, j, k = left, mid, left
        inv_count = 0

        while i < mid and j < right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
                inv_count += (mid - i)
            k += 1

        while i < mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j < right:
            temp[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right):
            arr[i] = temp[i]

        return inv_count

    def merge_sort(arr, temp, left, right):
        inv_count = 0
        if right > left + 1:
            mid = (left + right) // 2
            inv_count += merge_sort(arr, temp, left, mid)
            inv_count += merge_sort(arr, temp, mid, right)
            inv_count += merge(arr, temp, left, mid, right)
        return inv_count

    n = len(arr)
    temp = [0] * n
    return merge_sort(arr, temp, 0, n)