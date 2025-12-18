"""
QUESTION:
Create a function called `fibonacci` that takes an integer `n` as input and returns a list of Fibonacci numbers from 0 to `n` using an iterative approach without recursion or built-in functions, achieving a time complexity of O(n) and a space complexity of O(1).
"""

def fib(n):
    if n <= 0:
        return []

    fib_list = [0, 1]

    if n <= 1:
        return fib_list[:n + 1]

    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list