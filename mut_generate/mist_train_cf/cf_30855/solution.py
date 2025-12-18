"""
QUESTION:
Calculate the median of a list of integers. Given a list of integers `a`, write a function `calculate_median(a)` that returns the median as a floating-point number. The list length `n` is unknown, but it is greater than 0. The median is the middle number in the sorted list, or the average of the two middle numbers if `n` is even.
"""

def calculate_median(a):
    a.sort()
    s = len(a)
    if s % 2 == 0:
        median = (a[s//2 - 1] + a[s//2]) / 2
    else:
        median = a[s//2]
    return median