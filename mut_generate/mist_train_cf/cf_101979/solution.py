"""
QUESTION:
Write a function `multiply_and_reverse(list1, list2)` that takes two lists of integers as input. The function should return the sum of the products of corresponding elements from the two lists in reverse order. The function should only accept lists with the same length, containing only positive integers, and having at most 1000 elements.
"""

def multiply_and_reverse(list1, list2):
    # Check if lists have the same length
    if len(list1) != len(list2):
        return "Lists must have the same length"

    # Check if lists have more than 1000 elements
    if len(list1) > 1000 or len(list2) > 1000:
        return "Lists can have at most 1000 elements"

    # Check if all elements are positive integers
    if any(not isinstance(elem, int) or elem <= 0 for elem in list1 + list2):
        return "All elements must be positive integers"

    # Multiply corresponding elements and compute sum
    result = sum(list1[i] * list2[i] for i in range(len(list1)))

    # Return result in reverse order
    return list(str(result))[::-1]