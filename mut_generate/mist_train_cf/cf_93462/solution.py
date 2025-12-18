"""
QUESTION:
Write a function 'divideList' that takes a list of integers and two integers n and m as input, and returns a list of sublists. The function should divide the input list into n groups, with each group having a minimum of m elements. The elements within each group should be in non-decreasing order. The value of m should be greater than 1 and less than or equal to the length of the list divided by n. If m does not satisfy these conditions, the function should return an empty list.
"""

def divideList(lst, n, m):
    if m <= 1 or m > len(lst) // n:
        return []
    
    lst.sort()  # Sort the list in non-decreasing order
    
    groups = []
    group_size = len(lst) // n  # Size of each group
    
    for i in range(0, len(lst), group_size):
        group = lst[i:i+group_size]  # Get a slice of the list with 'group_size' elements
        groups.append(group)
    
    return groups