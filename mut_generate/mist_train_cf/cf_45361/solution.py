"""
QUESTION:
Create a function `custom_sort(arr)` that sorts the tuples in the input list `arr` in descending order based on the sum of their components without using the built-in `sort()` method or any similar function. The function should return the sorted list. The list `arr` contains tuples of varying lengths, and the sorting should be done based on the sum of the components of each tuple.
"""

def custom_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            # Swapping if sum of previous tuple is less than next tuple
            if sum(arr[j]) < sum(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr