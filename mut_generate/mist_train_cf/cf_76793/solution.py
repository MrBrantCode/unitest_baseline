"""
QUESTION:
Write a function called `find_third_smallest` that takes a list of numbers as input and returns the third smallest number. If the list contains less than three elements, return an error message. The time complexity of the function should be no worse than O(n), where n is the size of the list.
"""

def entance(lst):
    if len(lst) < 3:
        return "List does not contain enough elements"
    small, smaller, smallest = float('inf'), float('inf'), float('inf')
    for i in lst:
        if i <= smallest:
            small, smaller, smallest = smaller, smallest, i
        elif i < smaller:
            small, smaller = smaller, i
        elif i < small:
            small = i
    return small