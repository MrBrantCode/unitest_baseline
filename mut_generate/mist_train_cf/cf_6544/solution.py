"""
QUESTION:
Write a function `reverse_list` that takes a list of numbers as input and reverses it in place using a single loop with a constant amount of extra space, and a time complexity of O(n), where n is the length of the input list. The function should preserve the order of duplicate numbers and handle negative numbers in the input list.
"""

def reverse_list(lst):
    n = len(lst)
    i = 0
    j = n - 1

    while i < j:
        # Swap elements at indices i and j
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

    return lst