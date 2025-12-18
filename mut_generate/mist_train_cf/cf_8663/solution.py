"""
QUESTION:
Write a function 'divideList' that takes a list and an integer 'n' as input and divides the list into 'n' groups, ensuring each group has a minimum of 'm' elements where 'm' is an integer greater than 1 and less than or equal to the length of the list divided by 'n'. The elements within each group should be in non-decreasing order. The function should also return the number of distinct elements in the divided groups. The time complexity of the function should be O(n*m*log(m)).
"""

def divideList(lst, n):
    lst.sort()  
    m = -(-len(lst) // n)  
    groups = []  
    distinct_count = 0  

    for i in range(n):
        start = i * m
        end = (i + 1) * m
        if end > len(lst):
            end = len(lst)
        group = lst[start:end]
        groups.append(group)
        distinct_count += len(set(group))

    return groups, distinct_count