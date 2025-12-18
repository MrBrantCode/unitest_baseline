"""
QUESTION:
Write a function `sum_of_squares(N)` that calculates the sum of squares of integers from 1 to N, where N is a positive integer greater than 10. The function should have a time complexity of O(N) and a space complexity of O(1).
"""

def sum_of_squares(N):
    sum_squares = 0
    for i in range(1, N + 1):
        sum_squares += i ** 2
    return sum_squares