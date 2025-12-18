"""
QUESTION:
Write a function `reverse_list` that takes a list of integers as input, reverses the order of its elements, and returns the reversed list. The solution must have a time complexity of O(n), where n is the length of the list, and cannot use any built-in functions or methods for list manipulation.
"""

def reverse_list(my_list):
    start = 0
    end = len(my_list) - 1

    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1

    return my_list