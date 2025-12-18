"""
QUESTION:
Implement a function `reverse_list` that takes a list of integers as input and reverses the order of its elements in place, without using any built-in list manipulation functions or methods. The function should have a time complexity of O(n), where n is the length of the list, and constant space complexity, not creating any additional data structures with size proportional to the input.
"""

def reverse_list(my_list):
    n = len(my_list)
    left = 0
    right = n - 1

    while left < right:
        # Swap the elements at the left and right pointers
        my_list[left], my_list[right] = my_list[right], my_list[left]
        left += 1
        right -= 1

    return my_list