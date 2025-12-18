"""
QUESTION:
Write a function `most_frequent(arr)` that takes a multidimensional array `arr` as input and returns the most frequently occurring item in the array. The function should work correctly even if there are multiple items with the same highest frequency. Note that the input array can be nested and contain varying lengths of sublists.
"""

from collections import Counter

def most_frequent(arr):
    temp = Counter(x for sublist in arr for x in sublist) 
    return [item for item, count in temp.items() if count == max(temp.values())]