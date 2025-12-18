"""
QUESTION:
Create a function `odd_times_elements(lst)` that takes a list of integers `lst` as input and returns a new list containing only the elements that occur an odd number of times in the original list. The function should be optimized for both time and space complexity, especially for large lists (of the order of 10^6 elements).
"""

def odd_times_elements(lst):
    counts = dict()
    for el in lst:
        if el in counts: 
            counts[el] += 1
        else: 
            counts[el] = 1
    
    res = [el for el, count in counts.items() if count % 2 != 0]
    return res