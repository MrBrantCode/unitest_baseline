"""
QUESTION:
Implement a function called `mergeSort` that takes an array of integers as input and returns a new sorted array using the merge sort technique. The function should recursively divide the input array into smaller subarrays, sort them individually, and then merge the sorted subarrays into a single sorted array.
"""

def mergeSort(array):
    # If the array has only one element, it's already sorted
    if len(array) <= 1:
        return array

    # Dividing the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursive call on each half
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    # Merge and sort the two halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    # Merge elements into sorted_list from smallest to largest
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index +=1

    # If there are remaining elements in left or right, add them to the end of sorted_list
    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list