"""
QUESTION:
Implement a function `weighted_sort(elements, weights)` that sorts the `elements` list in ascending order, considering the `weights` list as secondary criteria for equal elements. The function should use an in-place sort technique, limit the use of built-in sorting methods, and preserve the original order of elements with equal weights.
"""

def weighted_sort(elements, weights):
    n = len(elements)

    # Perform the sorting using bubble sort
    for i in range(n):
        for j in range(0, n-i-1):

            # Compare elements based on the conditions
            if elements[j] > elements[j+1] or (elements[j] == elements[j+1] and weights[j] < weights[j+1]):
                # swap elements if they are in wrong order
                elements[j], elements[j+1] = elements[j+1], elements[j]
                weights[j], weights[j+1] = weights[j+1], weights[j]
                
    return elements