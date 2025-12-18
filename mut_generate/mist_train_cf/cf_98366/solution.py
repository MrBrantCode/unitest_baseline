"""
QUESTION:
Write a function `sum_n(n)` that calculates the sum of all integers from 0 to `n-1` and a function `sum_n_squared(n)` that calculates the sum of the products of all pairs of integers from 0 to `n-1`. The functions should be implemented in a way that highlights their different time complexities. 

Restrictions: The function `sum_n(n)` should have a time complexity of O(n) and the function `sum_n_squared(n)` should have a time complexity of O(n^2).
"""

def sum_n(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

def sum_n_squared(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += i * j
    return sum