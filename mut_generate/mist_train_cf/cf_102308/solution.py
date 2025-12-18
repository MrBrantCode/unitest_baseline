"""
QUESTION:
Create a function named get_even_elements that takes a list of integers A as input and returns a new list containing only the unique even elements from A in ascending order. If A does not contain any even elements, return an empty list.
"""

def get_even_elements(A):
    B = []
    for element in A:
        if element % 2 == 0 and element not in B:
            B.append(element)
    B.sort()
    return B