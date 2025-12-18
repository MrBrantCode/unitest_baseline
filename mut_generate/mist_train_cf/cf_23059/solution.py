"""
QUESTION:
Write a function 'divideList' that takes a list and two integers n and m as input, where m is greater than 1 and less than or equal to the length of the list divided by n. The function should divide the list into n groups, each containing at least m elements in non-decreasing order, and return the number of distinct elements in the divided groups.
"""

def divideList(lst, n, m):
    lst.sort()
    groups = []
    distinct_elements = set()
    
    # Calculate the minimum number of elements in each group
    min_elements = min(m, len(lst) // n)
    
    # Divide the list into groups
    for i in range(0, len(lst), min_elements):
        group = lst[i:i+min_elements]
        groups.append(group)
        distinct_elements.update(group)
    
    return len(distinct_elements)