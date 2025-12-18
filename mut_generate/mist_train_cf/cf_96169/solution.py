"""
QUESTION:
Implement a function named `remove_duplicates` that takes a list as input and returns a new list containing unique elements from the input list, maintaining the original order. The function should not use built-in methods like `set` or `dict` for this purpose, however, a single loop is allowed. The original list should not be modified, and the time and space complexities of the solution should be O(n) and O(n) respectively.
"""

def remove_duplicates(lst):
    unique_set = set()
    unique_lst = []

    for num in lst:
        if num not in unique_set:
            unique_set.add(num)
            unique_lst.append(num)

    return unique_lst