"""
QUESTION:
Develop a function named 'combineAndSortTwoLists' that takes two lists of integers as arguments, merges them into a single list, and sorts the combined list in ascending order using the merge sort algorithm. The function should not use built-in Python sorting functions, and it should have a time complexity of O(n log n).
"""

def merge(left, right):
    # The helper function to merge two sorted arrays
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def merge_sort(arr):
    # The main function to execute merge sort
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def combineAndSortTwoLists(list1, list2):
    # Combining the two lists and passing it to merge_sort function
    combined_list = list1 + list2
    return merge_sort(combined_list)