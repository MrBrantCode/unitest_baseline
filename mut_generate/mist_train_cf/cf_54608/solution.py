"""
QUESTION:
Create a function F that accepts an integer n and returns a list of size n. The list is arranged based on the following rules: 
- at even indexes (1-based), append the factorial of the index 
- at odd indexes (1-based), append the cumulative total from 1 to the index.
Implement the function F(n int) []int.
"""

import math

def F(n):
    result = []
    for i in range(1, n+1):
        if i % 2 != 0:
            result.append(math.factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result