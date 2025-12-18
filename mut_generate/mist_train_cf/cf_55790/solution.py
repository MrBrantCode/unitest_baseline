"""
QUESTION:
Write a function `lastElement` that returns the last non-null element from a given array. The array can hold any type of elements and its length can vary. If no non-null element exists, the function should return `None`.
"""

def lastElement(myArray):
    # Iterate over the list in reverse order
    for n in myArray[::-1]:
        if n is not None:
            # First non-null value from end
            return n
    # Returns None if no non-null value is found
    return None