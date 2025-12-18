"""
QUESTION:
Write a recursive function `find_max` that finds the maximum integer in a given list. The function must not use any loops, built-in functions, or methods. The time complexity of the function should be O(n), where n is the length of the list.
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