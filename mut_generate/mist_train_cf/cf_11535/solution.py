"""
QUESTION:
Implement a function `remove_duplicates_and_sort_list` that takes a list of integers as input, removes duplicates from the list, and sorts the remaining elements in ascending order. The function should have a time complexity of O(nlogn) and should not use built-in sorting functions. Instead, it should implement a sorting algorithm such as merge sort or quick sort.
"""

def remove_duplicates_and_sort_list(lst):
    unique_set = set()
    for num in lst:
        unique_set.add(num)
    unique_list = list(unique_set)
    
    # Implement a sorting algorithm (merge sort)
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            elif left[i] > right[j]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    
    sorted_list = merge_sort(unique_list)
    return sorted_list