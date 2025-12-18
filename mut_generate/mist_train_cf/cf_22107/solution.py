"""
QUESTION:
Write a function called `sort_strings` that takes a list of strings as input and returns a new list with the strings sorted in descending order of their lengths. If two strings have the same length, they should be ordered alphabetically. The function should have a time complexity of O(n log n) and use constant space complexity. It should not rely on any built-in sorting functions or libraries.
"""

def sort_strings(strings):
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
            if len(left[i]) > len(right[j]):
                result.append(left[i])
                i += 1
            elif len(left[i]) < len(right[j]):
                result.append(right[j])
                j += 1
            else:
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

    return merge_sort(strings)