"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns a list of Fibonacci numbers from 0 to `n`. Implement the solution using a purely iterative approach with a time complexity of O(n) and a space complexity of O(1). Do not use recursion or any built-in functions or libraries.
"""

def fibonacci(n):
    if n <= 0:
        return []

    fib_list = [0, 1]  

    if n <= 1:
        return fib_list[:n + 1]  

    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list