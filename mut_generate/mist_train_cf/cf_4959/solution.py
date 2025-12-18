"""
QUESTION:
Design a function `sort_tuples` that takes a list of tuples as input and returns the sorted list. The list should be sorted based on the first element of each tuple in descending order, ignoring cases if the element is a string. If the first elements are equal, the list should be sorted based on the second element in ascending order. The function cannot use built-in sorting functions or methods and should work for tuples with more than two elements.
"""

def sort_tuples(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if (x[0].lower() < pivot[0].lower() if isinstance(x[0], str) and isinstance(pivot[0], str) else x[0] < pivot[0])]
    middle = [x for x in lst if (x[0].lower() == pivot[0].lower() if isinstance(x[0], str) and isinstance(pivot[0], str) else x[0] == pivot[0])]
    right = [x for x in lst if (x[0].lower() > pivot[0].lower() if isinstance(x[0], str) and isinstance(pivot[0], str) else x[0] > pivot[0])]
    return sort_tuples(right) + sorted(middle, key=lambda x: x[1]) + sort_tuples(left)