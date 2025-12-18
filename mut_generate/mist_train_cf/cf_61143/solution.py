"""
QUESTION:
Write a function `find_mode` that finds the mode in a list containing mixed data types, specifically integers and floating-point numbers. The function should return the mode(s) if it exists, or "No mode found" if all elements in the list are unique. The list can be empty. The function should handle non-list inputs and non-numeric elements.
"""

from collections import Counter

def find_mode(mixed_list):
    try:
        n = len(mixed_list)
    except TypeError:
        print("The input is not a list.")
        return None
        
    if n==0: # no mode for empty list
        return None

    count = Counter(mixed_list)
    get_mode = dict(count)
    mode = [k for k, v in get_mode.items() if v == max(list(count.values()))]

    if len(mode) == n:
        return "No mode found"
    else:
        return mode