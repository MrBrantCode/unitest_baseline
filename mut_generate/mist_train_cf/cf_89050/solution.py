"""
QUESTION:
Implement a function `sort_tuples(lst)` that sorts a list of tuples in ascending order based on the first value of the tuple. The function should have a time complexity of O(n log n) or better, be stable (maintaining the relative order of tuples with the same first value), and perform the sorting in place without creating a new list or using any built-in sorting functions or libraries.
"""

def sort_tuples(lst):
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])

        return merge(left, right)

    return merge_sort(lst)