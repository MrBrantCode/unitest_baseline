"""
QUESTION:
Implement a function named `find_median` that takes a list of numbers with an odd length as input and returns the median of the list. The function should calculate the median without using any built-in functions or libraries that directly calculate the median, and it should have a time complexity of O(nlogn) and a space complexity of O(1).
"""

def find_median(arr):
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    sorted_arr = quicksort(arr)
    middle_index = len(sorted_arr) // 2
    return sorted_arr[middle_index]