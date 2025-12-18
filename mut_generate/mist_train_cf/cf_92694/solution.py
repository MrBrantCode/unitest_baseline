"""
QUESTION:
Write a function `generate_array(N)` that generates a 2D array of size N x N, where N is an integer between 3 and 10 (inclusive), and all elements are equal to 1. The time complexity of the function should be O(N^2).
"""

def entance(N):
    # Create an array of size N x N filled with 1s
    return [[1] * N for _ in range(N)]