"""
QUESTION:
Write a function called `fibonacci(n)` that takes an integer `n` and returns the nth Fibonacci number. The function should have a time complexity of O(n) and should not use any additional data structures beyond a constant amount of space. If `n` is negative, the function should return `None`.
"""

def fibonacci(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return n
    
    prev = 0
    curr = 1
    
    for _ in range(2, n+1):
        next_num = prev + curr
        prev = curr
        curr = next_num
    
    return curr