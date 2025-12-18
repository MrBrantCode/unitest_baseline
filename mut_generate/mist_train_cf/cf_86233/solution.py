"""
QUESTION:
Implement a function named `elementwise_product` that takes two vectors of size n as input and returns their element-wise product. The vectors may contain negative integers, duplicates, and floating-point numbers, and may be empty. The function should have a time complexity of O(n) or better.
"""

def elementwise_product(vector1, vector2):
    n = len(vector1)
    result = []
    for i in range(n):
        result.append(vector1[i] * vector2[i])
    return result