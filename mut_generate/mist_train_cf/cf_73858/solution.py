"""
QUESTION:
Write a function `median(l: list)` that calculates the median of elements in a list without sorting it. The function should handle lists containing negative integers and floating-point numbers, as well as lists with varied lengths. If the list is empty, the function should return 'No median exists'. The function should be able to efficiently handle large lists.
"""

def median(l: list):
    # Handle empty list
    if not l:
        return 'No median exists'
    
    # Find size of list
    size = len(l)

    # Since we are not sorting, to find the median, we find the element that is 
    # at the size//2 index if size is odd and average of elements at size//2 and (size//2) - 1 index   
    if size % 2 != 0:
        return select_nth(l, size // 2)
    else:
        return 0.5 * (select_nth(l, size // 2 - 1) + select_nth(l, size // 2))

def select_nth(l: list, n: int):
    """Implement order statistic selection algorithm as a helper function"""
    pivot = l[0]
    below = [x for x in l if x < pivot]
    above = [x for x in l if x > pivot]
    i, j = len(below), len(l) - len(above)
    if n < i:
        return select_nth(below, n)
    elif n >= j:
        return select_nth(above, n - j)
    else:
        return pivot