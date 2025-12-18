"""
QUESTION:
Create a function called `calculateFibonacci` that calculates the nth Fibonacci number, where n is a given number. The function should have a time complexity of O(n) and a space complexity of O(1) to efficiently handle large values of n (e.g. n > 10000) without causing a stack overflow or excessive computation time.
"""

def calculateFibonacci(n):
    if n == 0 or n == 1:
        return n
    
    a, b = 0, 1
    count = 2
    
    while count <= n:
        next = a + b
        a = b
        b = next
        count += 1
    
    return b