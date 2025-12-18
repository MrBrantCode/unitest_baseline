"""
QUESTION:
Find all local maxima in a given list. A local maximum is an element that is greater than its neighbors. If the list only contains one element, consider it as a local maximum. If there are multiple local maxima with the same value, include all their indices in the output. 

Create a function `find_local_maxima` that takes a list of integers as input. The input list can be empty.
"""

def find_local_maxima(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [0]
    else:
        result = []
        for i in range(len(lst)):
            if (i == 0 and lst[i] >= lst[i + 1]) or \
               (i == len(lst) - 1 and lst[i] >= lst[i - 1]) or \
               (lst[i] > lst[i - 1] and lst[i] > lst[i + 1]):
                result.append(i)
        return result