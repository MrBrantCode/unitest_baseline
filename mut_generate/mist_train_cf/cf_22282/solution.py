"""
QUESTION:
Write a function named `sum_of_squares` that calculates the sum of square numbers from 1 to N, where N is a positive integer greater than 10. The function should have a time complexity of O(N) and a space complexity of O(1).
"""

def sum_of_squares(N):
    return N * (N + 1) * (2*N + 1) // 6