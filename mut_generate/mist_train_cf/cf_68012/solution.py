"""
QUESTION:
Write a function `trace_occurrence(arr, depth=0, occurDict=None)` that takes a complex three-dimensional array `arr` and returns a dictionary where keys are unique numbers in the array and values are their occurrence counts. The function should handle arrays with up to 5 layers of nesting and should be optimized to run efficiently on large data sets.
"""

from collections import defaultdict

def trace_occurrence(arr, depth=0, occurDict=None):
    """Trace the occurrence of all unique numbers in a complex three-dimensional array"""
    if depth > 5: return occurDict # stop further recursions after depth of 5
    if occurDict is None: occurDict = defaultdict(int) # initialize defaultdict to handle non-existing keys

    # if arr is list or tuple, check depth and handle appropriately
    if isinstance(arr, (list, tuple)): 
        for item in arr: 
            trace_occurrence(item, depth+1, occurDict)
    else:
        occurDict[arr] += 1 
        
    return occurDict