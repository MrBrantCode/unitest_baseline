"""
QUESTION:
Design a function `solution(n)` that takes an integer `n` (1 ≤ N ≤ 10^5) as input, generates an array of the first `n` terms of the Fibonacci sequence, and calculates the product of every third element in the array. If `n` is less than 3, the function should return -1.
"""

def solution(n):
    if n < 3:  
        return -1

    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    product = 1
    for i in range(2, n, 3):  
        product *= fib[i]  

    return product