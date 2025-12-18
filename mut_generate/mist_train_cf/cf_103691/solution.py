"""
QUESTION:
Write a function `sum_of_even_numbers(n)` that calculates the sum of the first n even numbers with a time complexity of O(n) and a space complexity of O(1). The input `n` is an integer.
"""

def entrance(n):
    total = 0
    for i in range(1, n+1):
        total += 2*i
    return total