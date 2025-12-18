"""
QUESTION:
Implement a function `remove_duplicates` that takes a list as input and returns a new list with duplicate elements removed while maintaining the original order. The function should not modify the original list, have a time complexity of O(n), and a space complexity of O(n). The function should only use a single loop and cannot use built-in methods for removing duplicates or sorting.
"""

def remove_duplicates(lst):
    unique_set = set()
    unique_lst = []

    for num in lst:
        if num not in unique_set:
            unique_set.add(num)
            unique_lst.append(num)

    return unique_lst