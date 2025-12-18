"""
QUESTION:
Write a function named `reverse_list` that takes a list as input and reverses its order without using any built-in Python functions or methods. The function should have a time complexity of O(n) and a space complexity of O(1), and it should not use any additional data structures.
"""

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst