"""
QUESTION:
Write a function `nth_fibonacci(n)` to calculate the nth Fibonacci number. The function should meet the following requirements:
- The function should take an integer `n` as input and return the corresponding Fibonacci number.
- The function should have a time complexity of O(n) and a space complexity of O(1).
- If `n` is less than or equal to 0, the function should return `None`.
- The Fibonacci sequence starts with 0 and 1, where each subsequent number is the sum of the previous two numbers.
"""

def nth_fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    prev = 0
    curr = 1
    for i in range(3, n+1):
        temp = prev + curr
        prev = curr
        curr = temp
    
    return curr