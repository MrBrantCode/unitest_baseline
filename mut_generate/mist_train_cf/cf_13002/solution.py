"""
QUESTION:
Create a function `fibonacci(N)` that generates the Nth Fibonacci number, where N is a positive integer less than or equal to 1000. The function should have a time complexity of O(N) and a space complexity of O(1).
"""

def fibonacci(N):
    a, b = 0, 1

    if N <= 0:
        return 0
    if N == 1:
        return 1

    for i in range(2, N+1):
        temp = a + b
        a = b
        b = temp

    return b