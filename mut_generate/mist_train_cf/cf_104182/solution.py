"""
QUESTION:
Write a function `calculate_sum` that calculates the sum of the expression `i + j` for all pairs `(i, j)` where `i` and `j` are integers in the range `[0, n)` and `i <= j`. The function should take an integer `n` as input and return the calculated sum. The time complexity of the function should be O(n).
"""

def calculate_sum(n):
    total_sum = 0
    for i in range(n):
        total_sum += (n - i) * (i + i)
    return total_sum