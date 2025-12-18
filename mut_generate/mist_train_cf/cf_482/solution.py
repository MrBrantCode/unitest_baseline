"""
QUESTION:
Create a function named `reverse_list_recursion` that takes a list of integers as input and returns a new list with the elements in reverse order using recursion, without using any built-in functions or libraries. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list. It should not modify the original list and instead create a new list with the reversed elements.
"""

def reverse_list_recursion(lst):
    def reverse_helper(lst, start, end):
        if start >= end:
            return lst
        lst[start], lst[end] = lst[end], lst[start]
        return reverse_helper(lst, start+1, end-1)
    
    lst_copy = lst[:]  # Create a copy of the original list
    return reverse_helper(lst_copy, 0, len(lst)-1)