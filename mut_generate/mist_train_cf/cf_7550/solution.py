"""
QUESTION:
Implement a function `find_median` that finds the median of a list of numbers. The function should return the median value. If the list has an even number of elements, the median should be the average of the two middle values. The implementation should have a time complexity of O(n log n) or better and should not use any built-in sorting functions or libraries.
"""

def find_median(lst):
    def merge(left, right):
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

    sorted_lst = merge_sort(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median = (sorted_lst[n//2-1] + sorted_lst[n//2]) / 2
    else:
        median = sorted_lst[n//2]
    
    return median