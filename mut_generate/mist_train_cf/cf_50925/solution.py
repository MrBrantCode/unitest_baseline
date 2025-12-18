"""
QUESTION:
Write a function named `shared_elements` that takes two lists as input and returns the distinct elements common to both lists in increasing order. The function should have a time complexity of O(nlogn) or better and should not use Python's built-in sorting or duplicate removal functions.
"""

def shared_elements(list1, list2):
    def partition(arr):
        pivot = arr[0]
        left = [i for i in arr[1:] if i < pivot]
        middle = [i for i in arr if i == pivot]
        right = [i for i in arr[1:] if i > pivot]
        return left, middle, right

    def quick_sort(arr):
        if len(arr) == 0:
            return arr
        left, middle, right = partition(arr)
        return quick_sort(left) + middle + quick_sort(right)

    common = []
    sorted1 = quick_sort(list1)
    sorted2 = quick_sort(list2)

    i = j = 0
    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] == sorted2[j]:
            if len(common) == 0 or common[-1] != sorted1[i]:
                common.append(sorted1[i])
            i += 1
            j += 1
        elif sorted1[i] < sorted2[j]:
            i += 1
        else:
            j += 1
    return common