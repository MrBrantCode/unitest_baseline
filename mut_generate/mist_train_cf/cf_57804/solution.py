"""
QUESTION:
Implement a function `partition` to partition an array for quicksort algorithm, another function `kth_element` to find the kth smallest element in the array, and a function `median` to calculate the median of the array using the `kth_element` function. 

In the `partition` function, rearrange the elements in the array `arr` between indices `low` and `high` around a pivot element. Return the indices `lt` and `gt` where `lt` is the index of the first element greater than the pivot and `gt` is the index of the last element less than the pivot. 

The `kth_element` function should use the `partition` function to recursively narrow down the search space until it finds the kth smallest element. The function should take an array `arr` and an integer `k` as input and return the kth smallest element.

The `median` function should calculate the median of the array `l` by calling the `kth_element` function. If the length of the array is odd, return the middle element. If the length of the array is even, return the average of the two middle elements.
"""

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    lt = low
    gt = high
    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            i += 1
            lt += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def kth_smallest(arr, k):
    l = 0
    r = len(arr) - 1
    while True:
        if r <= l:
            return arr[l]
        m1, m2 = partition(arr, l, r)
        if m1 <= k <= m2:
            return arr[k]
        elif k < m1:
            r = m1 - 1
        else:
            l = m2 + 1

def median_of_array(l):
    if len(l) % 2:
        return kth_smallest(l, len(l) // 2)
    else:
        return (kth_smallest(l, len(l) // 2 - 1) + kth_smallest(l, len(l) // 2)) * 0.5