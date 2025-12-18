"""
QUESTION:
Implement a function `binary_sum` that takes a vector of integers as input and returns a tuple containing the sum of all elements in the vector, the maximum element, and the minimum element. The function should achieve this in O(log n) time complexity and O(1) space complexity, where n is the number of elements in the vector.
"""

def binary_sum(vector):
    total = 0
    maximum = vector[0]
    minimum = vector[0]
    
    for num in vector:
        total += num
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
            
    return (total, maximum, minimum)