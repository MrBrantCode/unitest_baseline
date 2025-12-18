"""
QUESTION:
Create a function `increase_elements` that takes a vector (list of numbers) as input. The function should modify the vector such that all elements are greater than five. If an element is already greater than five, it should remain unchanged. If an element is less than or equal to five, it should be increased by a certain amount to make it greater than five.
"""

def increase_elements(vector):
    for i in range(len(vector)):
        if vector[i] <= 5:
            vector[i] += 6 - vector[i]
    return vector