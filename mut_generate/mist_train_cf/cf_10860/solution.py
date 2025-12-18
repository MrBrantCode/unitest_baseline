"""
QUESTION:
Write a function called `reverse_list` that takes a list as input and reverses the order of its elements without using any built-in functions or methods. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list.
"""

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst