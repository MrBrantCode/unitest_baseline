"""
QUESTION:
Design a function named `detect_duplicates` that takes two arrays as input: `array1` containing integers and `array2` containing integer tuples. The function should use hash tables to detect duplicate elements within each array separately and return `True` if any duplicates are found, otherwise return `False`. The function should handle edge cases such as empty arrays, arrays with just one element, and arrays with all duplicate elements, and ignore non-integer elements and non-integer tuples.
"""

def detect_duplicates(array1, array2):
    # create hash table to store elements
    Hash1 = {}
    Hash2 = {}

    # iterate over the first array
    for element in array1:
        if type(element) == int:
            # check if element already exists in hash table
            if element in Hash1:
                # if it does, it is a duplicate
                return True
            # otherwise, add element to hash table
            Hash1[element] = 1

    # iterate over the second array
    for element in array2:
        if type(element) == tuple and len(element)==2 and type(element[0])==int and type(element[1])==int:
            if element in Hash2:
                return True
            Hash2[element] = 1

    # No duplicates found
    return False