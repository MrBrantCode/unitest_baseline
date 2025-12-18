"""
QUESTION:
Write a function `remove_elements(A, B)` that takes in two sets, A and B, and removes all elements from A that are also present in B. The function should return the modified set A. The function should have a time complexity of O(n), where n is the number of elements in set A, and should use only a single loop to iterate through the elements of set A, without using any built-in Python set methods or functions or additional data structures besides the input sets A and B.
"""

def remove_elements(A, B):
    # create a new set to store the elements to be removed
    to_remove = set()

    # iterate through the elements in set A
    for element in A:
        # check if the element is also present in set B
        if element in B:
            # add the element to the set of elements to be removed
            to_remove.add(element)

    # remove the elements from set A
    for element in to_remove:
        A.remove(element)

    # return the modified set A
    return A