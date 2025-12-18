"""
QUESTION:
Write a function named `shared_elements` that takes two lists of integers as input and returns a list of common elements between the two input lists, sorted in ascending order and with duplicates removed. The function should use the merge sort algorithm to sort the input lists before finding common elements.
"""

def shared_elements(list1: list, list2: list):
    # Merge sort function to sort the input lists
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])

        return merge(left, right)

    def merge(left, right):
        if not left or not right:
            return left or right

        result = []

        i, j = 0, 0
        while len(result) < len(left) + len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            if i == len(left) or j == len(right):
                result.extend(left[i:] or right[j:])
                break 

        return result

    # Sorting lists
    sorted1 = merge_sort(list1)
    sorted2 = merge_sort(list2)

    # Finding common elements
    common = []
    i, j = 0, 0
    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] == sorted2[j]:
            if not common or common[-1] != sorted1[i]:
                common.append(sorted1[i])
            i += 1
            j += 1
        elif sorted1[i] < sorted2[j]:
            i += 1
        else:
            j += 1
    
    return common