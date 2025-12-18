"""
QUESTION:
Create a function called `search_element` that takes a 2D list `matrix` and an integer `element` as inputs. The function should return `True` if `element` exists in any row of the `matrix`, and `False` otherwise.
"""

def search_element(matrix, element):
    for row in matrix:
        if element in row:
            return True
    return False