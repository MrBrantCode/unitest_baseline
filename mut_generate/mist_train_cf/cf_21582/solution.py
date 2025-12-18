"""
QUESTION:
Write a function `fibonacci(n)` to calculate the n-th Fibonacci number with a time complexity of O(log n) and a space complexity of O(1) without using recursion or iteration. The function should take an integer `n` as input and return the corresponding Fibonacci number.
"""

import math

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    phi = (1 + math.sqrt(5)) / 2
    phi_n = phi ** n
    neg_phi_n = (-phi) ** (-n)
    
    return int((phi_n - neg_phi_n) / math.sqrt(5))