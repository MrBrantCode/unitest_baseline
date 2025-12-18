"""
QUESTION:
Write a function named `reverse` that takes a list `lst` as input, reverses the order of its elements in-place using recursion, and does not use any built-in or library functions for list manipulation. The function should have a time complexity of O(n), where n is the length of the list, and a space complexity of O(1).
"""

def reverse(lst):
    def reverse_helper(lst, start, end):
        if start >= end:
            return
        lst[start], lst[end] = lst[end], lst[start]
        reverse_helper(lst, start+1, end-1)

    reverse_helper(lst, 0, len(lst)-1)