"""
QUESTION:
Write a function `reverse_list` that takes a list of integers as input and returns the list with its elements reversed in place, without using any additional data structures or built-in reverse methods. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the input list.
"""

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst