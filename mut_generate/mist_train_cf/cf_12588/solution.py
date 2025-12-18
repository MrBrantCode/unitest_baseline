"""
QUESTION:
Create a function named `create_array` that takes a single positive integer `n` as input and returns an array of `n` elements. The array should be constructed such that each element is the sum of its two preceding elements, with the first two elements being 0 and 1. If `n` is less than or equal to 0, return an empty array.
"""

def create_array(n):
    if n <= 0:
        return []

    array = [0, 1]  
    if n <= 2:
        return array[:n]  

    for i in range(2, n):
        array.append(array[i-1] + array[i-2])  

    return array