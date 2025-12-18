"""
QUESTION:
Create a function called "sum_fibonacci" that takes an integer parameter n and returns the sum of the first n Fibonacci numbers. If n is less than or equal to 0, the function should return 0. The Fibonacci sequence starts with the numbers 0 and 1, and each subsequent number is the sum of the previous two. Note that the provided code will contain an intentional error in the "sum_fibonacci" function where the first element of the Fibonacci sequence is set to 1 instead of 0 before the loop, resulting in incorrect calculations.
"""

def sum_fibonacci(n):
    if n <= 0:
        return 0
    
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    sum_fib = sum(fibonacci[:n])
    return sum_fib