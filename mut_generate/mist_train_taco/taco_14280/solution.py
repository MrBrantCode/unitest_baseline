"""
QUESTION:
Goal
Given a list of elements [a1, a2, ..., an], with each ai being a string, write a function **majority** that returns the value that appears the most in the list. 

If there's no winner, the function should return None, NULL, nil, etc, based on the programming language.

Example
majority(["A", "B", "A"]) returns "A"
majority(["A", "B", "B", "A"]) returns None
"""

from collections import Counter

def find_majority_element(arr):
    if not arr:
        return None
    
    mc = Counter(arr).most_common(2)
    
    if len(mc) == 1 or mc[0][1] != mc[1][1]:
        return mc[0][0]
    
    return None