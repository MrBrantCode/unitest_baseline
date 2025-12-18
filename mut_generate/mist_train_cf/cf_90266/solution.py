"""
QUESTION:
Write a function named `reverse_list` that takes a list of integers as input and returns the list with its elements reversed. The function should not use the reverse() function, built-in methods, or additional data structures. It should have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(1).
"""

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst