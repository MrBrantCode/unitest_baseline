"""
QUESTION:
Create a function named `generate_fibonacci_series(num)` that generates the Fibonacci series for a given number `num`. The function should return a list of numbers representing the Fibonacci series up to the given number. If `num` is less than or equal to 0, return an empty list.
"""

def generate_fibonacci_series(num):
    a = 0
    b = 1
    fib_series = []

    if num <= 0:
        return fib_series
    elif num == 1:
        fib_series.append(a)
        return fib_series
    elif num == 2:
        fib_series.append(a)
        fib_series.append(b)
        return fib_series
    else:
        fib_series.append(a)
        fib_series.append(b)
        for i in range(2, num):
            next_num = a + b
            a = b
            b = next_num
            fib_series.append(next_num)
        return fib_series