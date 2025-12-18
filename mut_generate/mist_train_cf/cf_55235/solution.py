"""
QUESTION:
Create a function `f(n)` that returns a list of `n` length. For each index `i` (starting from 1), if `i` is even, the element at that index should be the factorial of `i`, and if `i` is odd, the element should be the sum of numbers from 1 to `i`. The function should have linear time and space complexity.
"""

def f(n):
    result = [1] * n
    even_val = 1
    odd_val = 1
    for i in range(2, n+1):
        if i % 2 == 0:
            even_val *= i
            result[i-1] = even_val
        else:
            odd_val += i
            result[i-1] = odd_val
    return result