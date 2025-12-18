"""
QUESTION:
Write a function named `count_elements` that takes a list of integers as input and outputs the recurring elements in their original order of occurrence along with their frequency. The function should be space-efficient and handle large datasets. The input list may contain duplicate values.
"""

def count_elements(xs):
    element_order = []
    element_count = {}

    for x in xs:
        if x not in element_count:
            element_order.append(x)
        element_count[x] = element_count.get(x, 0) + 1

    return [(x, element_count[x]) for x in element_order if element_count[x] > 1]