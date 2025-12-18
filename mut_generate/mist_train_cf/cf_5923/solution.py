"""
QUESTION:
Write a function named `insertion_sort_reverse` that sorts a list of integers in reverse order using the insertion sort algorithm. The list contains integers ranging from -10^9 to 10^9, and its length is between 10^5 and 10^7. The time complexity should not exceed O(n^2), and the space complexity should not exceed O(1). The solution should not use any built-in sorting functions or libraries.
"""

def insertion_sort_reverse(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr