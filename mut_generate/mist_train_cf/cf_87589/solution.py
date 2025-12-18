"""
QUESTION:
Design an algorithm to find the median element of a list of n elements, where n is between 1 and 10^6. The function should be named `find_median` and take a list `lst` as input. Note that the time complexity of the solution is not restricted to be optimal, but it should be able to handle large inputs.
"""

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median = (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        median = sorted_lst[n//2]
    return median