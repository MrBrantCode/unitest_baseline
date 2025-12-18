"""
QUESTION:
Write a recursive function `fibonacci` that takes an integer `n` as input and returns a list of the first `n` Fibonacci numbers. The function should have a time complexity of O(n) and space complexity of O(n). Note that the input number `n` should be a positive integer.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list