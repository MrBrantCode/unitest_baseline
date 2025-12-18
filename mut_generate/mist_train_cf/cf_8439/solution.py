"""
QUESTION:
Write a function called `fibonacci(n)` that displays the Fibonacci sequence up to the nth term. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The sequence starts with 0 and 1. 

Requirements:
- The solution should use iteration (loops) instead of recursion.
- The time complexity should be O(n), where n is the input number.
- The space complexity should be O(1), meaning that the solution should not use an array or list to store the sequence.
- The addition operator (+) cannot be used to calculate the Fibonacci numbers, so an alternative way to calculate the numbers must be found.
- The function should return the nth Fibonacci number.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            a, b = b, a ^ b ^ (a << 1) ^ (a & b)
        return b