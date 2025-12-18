"""
QUESTION:
Implement a function named `insertion_sort` that sorts an array of integers in ascending order with the following restrictions: 
- The array can contain duplicate values.
- The array length can be up to 10^6 elements.
- The time complexity of the implementation should be O(n^2).
- The space complexity should be O(1).
- The function should be able to handle both sorted and unsorted arrays, as well as arrays containing negative integers.
"""

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr