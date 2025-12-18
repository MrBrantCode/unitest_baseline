"""
QUESTION:
Write a function `increase_elements` that takes a list of integers as input and returns the modified list where all elements are greater than five. If an element is already greater than five, leave it as is; otherwise, increment it by the smallest amount necessary to make it greater than five.
"""

def increase_elements(vector):
    for i in range(len(vector)):
        if vector[i] <= 5:
            vector[i] += (6 - vector[i])
    return vector