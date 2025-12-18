"""
QUESTION:
Write a function `insert_element(arr, elem)` that inserts a new element `elem` into an existing unsorted array `arr`, ensuring the array does not contain any duplicates and maintains a record of insertion order. The elements in `arr` are hashable and the function should return the updated array. The time complexity of the method should be O(n), where n is the number of elements in the input array.
"""

from collections import OrderedDict

def insert_element(arr, elem):
    # Initialize an empty OrderedDict
    od = OrderedDict()

    # Iteratively add elements in arr to od
    # This will automatically remove any duplicates
    for e in arr:
        od[e] = None

    # If elem is not already in od, add it
    # The order of insertion is maintained
    if elem not in od:
        od[elem] = None

    # Convert OrderedDict back to a list and return
    return list(od.keys())