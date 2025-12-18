"""
QUESTION:
Create a function called `sort_set` that takes a set of strings as input and returns the set in ascending alphabetical order. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions or libraries. The input set may contain duplicate elements, but the output set should not.
"""

def sort_set(my_set):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            elif left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    sorted_list = merge_sort(list(my_set))
    sorted_set = set(sorted_list)
    return sorted_set