"""
QUESTION:
Create a function called `find_odd_occurrences` that takes a list of elements (integers and strings) as input and returns a new list containing only the elements that occur an odd number of times in the input list.
"""

from collections import Counter

def find_odd_occurrences(lst):
    count = Counter(lst)
    return [item for item in lst if count[item] % 2 != 0]