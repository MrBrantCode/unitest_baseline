"""
QUESTION:
Write a function `median(l)` that calculates the median of a list `l` of numbers. The function should handle empty lists and return the string 'No median exists'. If the list size is odd, it should return the middle element. If the list size is even, it should return the average of the two middle elements. Use the `select_nth(l, n)` helper function to find the nth smallest element in the list. The `select_nth` function should implement the order statistic selection algorithm. 

The function should work with lists of integers and floats, and should not sort the input list.
"""

def median(l: list):
    # Handle empty list
    if not l:
        return 'No median exists'

    # Find size of list
    size = len(l)

    # Since we are not sorting, to find the median, we find the element that is at the size//2 index if size is odd 
    # and average of elements at size//2 and (size//2 - 1) index 
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