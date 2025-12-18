"""
QUESTION:
Implement a function, `find_fifth_element`, that takes as input a list of integers `a` and a list of integers `q`, representing the initial array and the list of operations, respectively. The function should return the 5th element in the modified array after performing all the operations, or "-1" if the final array has less than 5 elements. The operations are defined as removing an element at index `i` from the array and inserting it at the beginning of the array. Note that the index `i` is 1-indexed. The function should be able to handle a large number of operations efficiently.
"""

def find_fifth_element(a, q):
    """
    This function performs operations on the list 'a' based on the list 'q'. 
    It returns the 5th element in the modified array after performing all the operations. 
    If the final array has less than 5 elements, it returns -1.

    Parameters:
    a (list): Initial array of integers.
    q (list): List of operations, where each operation is the index of the element to be moved to the beginning of the array.

    Returns:
    int: The 5th element in the modified array, or -1 if the array has less than 5 elements.
    """
    for i in q:
        element = a.pop(i-1)
        a.insert(0, element)

    return a[4] if len(a) >= 5 else -1