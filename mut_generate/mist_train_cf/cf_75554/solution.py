"""
QUESTION:
Implement a function `median` that calculates the median of a list of numbers using the QuickSelect algorithm. The function should take a list `l` as input and return the median. If the length of the list is odd, the median is the middle element. If the length of the list is even, the median is the average of the two middle elements. You can use a helper function `quickselect` to select the k-th smallest element from the list. Assume that the input list is not empty and contains only numbers.
"""

def median(l):
    n = len(l)
    if n < 1:
        return None
    if n % 2 == 1:
        return quickselect(l, n//2)
    else:
        return 0.5 * (quickselect(l, n//2 - 1) + quickselect(l, n//2))

def quickselect(l, k):
    if len(l) == 1:
        return l[0]
    pivot = l[len(l) // 2]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return l[k]
    else:
        return quickselect(right, k - len(left) - len(middle))