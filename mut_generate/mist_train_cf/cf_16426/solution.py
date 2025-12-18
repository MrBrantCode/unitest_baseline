"""
QUESTION:
Write a function named `reverse_list` that takes a list of integers as input and reverses the order of its elements without using any built-in functions or methods for list manipulation. The time complexity of the solution should be O(n), where n is the length of the list. The function should return the reversed list.
"""

def reverse_list(my_list):
    start = 0
    end = len(my_list) - 1

    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1

    return my_list