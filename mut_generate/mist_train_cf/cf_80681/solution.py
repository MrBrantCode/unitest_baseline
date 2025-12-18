"""
QUESTION:
Implement a function called `binary_search` that takes a sorted list of numbers `lst`, and two target numbers `target1` and `target2`, and returns a tuple containing two sorted lists: the indexes of `target1` and the indexes of `target2`, each in ascending order. If either target is not found, return a tuple containing a list of indexes or -1 in place of the list. The list can contain repeats and the function should handle duplicates.
"""

def binary_search(lst, target1, target2):
    def get_indices(target):
        left, right = 0, len(lst) - 1
        first = last = -1

        # binary search for the first occurrence
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or target > lst[mid - 1]) and lst[mid] == target:
                first = mid
                break
            elif lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left, right = first, len(lst) - 1
        # binary search for the last occurrence
        while left <= right:
            mid = (left + right) // 2
            if (mid == len(lst) - 1 or target < lst[mid + 1]) and lst[mid] == target:
                last = mid
                break
            elif lst[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        if first != -1 and last != -1:
            return list(range(first, last + 1))
        else:
            return -1

    return get_indices(target1), get_indices(target2)