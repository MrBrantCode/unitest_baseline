"""
QUESTION:
Implement the following functions: 

1. `merge_sort(lst)`: This function should take a list of elements as input and return a new list with the elements sorted in ascending order. The function should use the merge sort algorithm.

2. `merge(left, right)`: This function should take two sorted lists as input and return a new list that contains all elements from both lists, sorted in ascending order.

3. `remove_duplicates(lst)`: This function should take a list of elements as input and return a new list that contains the same elements, but with duplicates removed.

4. `get_common(l1, l2)`: This function should take two lists as input and return a new list that contains the common elements between the two lists, sorted in ascending order and with duplicates removed.

Note that the functions should operate on lists of comparable elements (for sorting purposes).
"""

def merge_sort(lst: list):
    """merge_sort function sorts the elements of a list in ascending order"""
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)

def merge(left: list, right: list):
    """Merge two sorted lists"""
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

def remove_duplicates(lst: list):
    """Remove duplicates from a list"""
    deduped = []
    for i in lst:
        if i not in deduped:
            deduped.append(i)
    return deduped

def get_common(l1: list, l2: list):
    """Returns sorted unique common elements for two lists"""
    common_elements = [i for i in l1 if i in l2]
    unique_common_elements = remove_duplicates(common_elements)
    sorted_unique_common_elements = merge_sort(unique_common_elements)
    return sorted_unique_common_elements