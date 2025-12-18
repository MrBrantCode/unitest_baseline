"""
QUESTION:
Write a function called `reverse_list` that takes one parameter, a list of integers, and returns the list in reverse order. You can only use basic operations like swapping elements, indexing, and iteration, without any temporary data structures or built-in methods such as `reverse()` or slicing.
"""

def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        # Swap the elements at start and end indices
        lst[start], lst[end] = lst[end], lst[start]
        
        # Move start index forward and end index backward
        start += 1
        end -= 1
    
    return lst