"""
QUESTION:
Write a function `binary_sum` that takes a vector of integers as input and returns a tuple containing the sum of all elements, the maximum element, and the minimum element in the vector. The function should achieve this in O(log n) time complexity and O(1) space complexity.
"""

def binary_sum(vector):
    def binary_sum_helper(vector):
        if len(vector) == 1:
            return vector[0]
        else:
            mid = len(vector) // 2
            left_sum = binary_sum_helper(vector[:mid])
            right_sum = binary_sum_helper(vector[mid:])
            return left_sum + right_sum
    
    total_sum = binary_sum_helper(vector)
    maximum = max(vector)
    minimum = min(vector)
    return (total_sum, maximum, minimum)