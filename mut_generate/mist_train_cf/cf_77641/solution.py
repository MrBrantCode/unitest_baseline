"""
QUESTION:
Create a function `common` that takes two lists `l1` and `l2` as input and returns a list of their sorted distinct common elements. The function should not use any built-in Python list functions or set operations. Instead, implement custom functions for sorting and duplicate removal. Apply functional programming concepts to achieve the goal. The returned list should be sorted in ascending order.
"""

def entance(l1: list, l2: list):
    """Returns sorted unique common elements for two lists"""
    
    def merge_sort(lst: list):
        """merge_sort function the will sort the elements of a list in ascending order"""
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

    common_elements = [i for i in l1 if i in l2]
    unique_common_elements = remove_duplicates(common_elements)
    sorted_unique_common_elements = merge_sort(unique_common_elements)
    
    return sorted_unique_common_elements