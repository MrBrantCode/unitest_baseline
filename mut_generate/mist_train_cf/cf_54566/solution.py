"""
QUESTION:
Write a function named `fibonacci` that generates the Fibonacci sequence up to the nth position. The function should use a looping mechanism, store the sequence in a list, and return the list. Ensure the function is optimized for better performance. The function should not use recursive calls.
"""

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib