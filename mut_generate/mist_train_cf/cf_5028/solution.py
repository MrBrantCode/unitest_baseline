"""
QUESTION:
Implement a function called `sort_employees` that takes a list of employee dictionaries and a comparison function as parameters, and returns a new list of employees sorted by their age in ascending order. The function should use a stable sorting algorithm with a time complexity of O(n log n), such as merge sort or Timsort, without using any built-in sorting functions or methods. The function should also maintain the relative order of employees with the same age. The comparison function should define the ordering of the employees based on their age.
"""

def sort_employees(employees, compare_func):
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
            if compare_func(left[i]["age"], right[j]["age"]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return merge_sort(employees)