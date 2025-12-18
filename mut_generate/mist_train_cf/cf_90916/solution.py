"""
QUESTION:
Create a function `merge_and_remove_duplicates(arr1, arr2)` that merges two given arrays, removes duplicates, and returns the merged array in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the total number of elements in the merged array.
"""

def merge_and_remove_duplicates(arr1, arr2):
    merged_list = []
    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] < arr2[pointer2]:
            merged_list.append(arr1[pointer1])
            pointer1 += 1
        elif arr1[pointer1] > arr2[pointer2]:
            merged_list.append(arr2[pointer2])
            pointer2 += 1
        else:
            merged_list.append(arr1[pointer1])
            pointer1 += 1
            pointer2 += 1

    while pointer1 < len(arr1):
        merged_list.append(arr1[pointer1])
        pointer1 += 1

    while pointer2 < len(arr2):
        merged_list.append(arr2[pointer2])
        pointer2 += 1

    return merged_list