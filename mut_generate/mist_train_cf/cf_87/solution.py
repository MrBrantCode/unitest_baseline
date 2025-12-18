"""
QUESTION:
Write a recursive function `find_max` that takes a list of integers as input and returns the maximum integer in the list. The function should have a time complexity of O(n), where n is the length of the list, and should not use any loops, built-in functions, or methods.
"""

def find_max(lst):
    # Base case: if the list has only one element, return it as the maximum
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case: divide the list into two halves and recursively find the maximum in each half
    mid = len(lst) // 2
    max_left = find_max(lst[:mid])
    max_right = find_max(lst[mid:])
    
    # Return the maximum of the two halves
    return max(max_left, max_right)