"""
QUESTION:
Write a function named `sum_sorted_desc` that takes two lists of integers as input. The function should return a new list containing the sum of corresponding elements from the input lists in descending order. If the input lists are of different lengths, consider the missing elements as 0. The function should handle negative integers and not use any built-in Python functions or libraries for list manipulation.
"""

def sum_sorted_desc(a, b):
    # Making two lists the same size
    if len(a) < len(b):
        a += [0] * (len(b) - len(a))
    elif len(b) < len(a):
        b += [0] * (len(a) - len(b))
    
    # Adding corresponding elements
    c = [a[i] + b[i] for i in range(len(a))]
    
    # Sorting in descending order
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            if c[i] < c[j]:
                c[i], c[j] = c[j], c[i]
    
    return c