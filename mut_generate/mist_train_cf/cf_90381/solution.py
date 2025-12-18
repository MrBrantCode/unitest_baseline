"""
QUESTION:
Reverse the order of elements in a given list in-place using recursion. Implement a function named `reverse` that takes a list as input and reverses its order without using any built-in or library functions for list manipulation. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.
"""

def reverse(lst):
    def reverse_helper(lst, start, end):
        if start >= end:
            return
        lst[start], lst[end] = lst[end], lst[start]
        reverse_helper(lst, start+1, end-1)

    reverse_helper(lst, 0, len(lst)-1)