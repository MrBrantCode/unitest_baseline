"""
QUESTION:
Implement a function named `reverse_list` that takes a list `lst` and an optional index `i` as parameters. The function should reverse the order of the elements in the list using only recursion, without using any additional data structures, and with a time complexity of O(n).
"""

def reverse_list(lst, i=0):
    if i == len(lst):
        return []
    reversed_tail = reverse_list(lst, i + 1)
    return reversed_tail + [lst[i]]