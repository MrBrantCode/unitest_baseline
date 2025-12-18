"""
QUESTION:
Create a function named `convert_to_multidimensional` that takes a list of integers `a` as input and returns a multidimensional list of size `len(a) X len(a)`. Each element in the multidimensional list should be a tuple consisting of three elements: the original element from list `a`, its index position in list `a`, and the sum of all previous elements in the current row of the multidimensional list up to the current index position. The function should have a time complexity of O(n^2), where n is the length of the input list `a`.
"""

def entance(a):
    n = len(a)
    result = []
    for i in range(n):
        row = []
        total = 0
        for j in range(n):
            element = (a[j], j, total)
            row.append(element)
            total += a[j]
        result.append(row)
    return result