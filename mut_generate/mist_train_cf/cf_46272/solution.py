"""
QUESTION:
Implement a function `binary_search(lst, target)` that performs a binary search on the input list `lst` to find the index of the `target` element. The function should accept both ordered and unordered lists as input. If the list is not ordered, it must first sort the list before conducting the binary search. The function should be able to handle both numerical and string data types in the list, treating string inputs as if they were ordered lexicographically.
"""

def binary_search(lst, target):
    # check if list is sorted, if not, sort it
    if lst != sorted(lst, key=lambda x: (str(type(x)), x)):
        lst = sorted(lst, key=lambda x: (str(type(x)), x))

    # Binary Search Algorithm
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None