"""
QUESTION:
Write a function 'divideList' that takes a list of integers and two integers n and m as input, where m is greater than 1 and less than or equal to the length of the list divided by n. The function should divide the list into n groups, ensuring each group has a minimum of m elements and that the elements within each group are in non-decreasing order. If m is not within the valid range, return an empty list.
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