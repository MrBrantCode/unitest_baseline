"""
QUESTION:
Write a function named `reverse_list` that takes a list as an argument and reverses its order in-place without using the built-in reverse function, any additional list or array for temporary storage, or recursion. The solution should have a time complexity of O(n), where n is the length of the list.
"""

def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst