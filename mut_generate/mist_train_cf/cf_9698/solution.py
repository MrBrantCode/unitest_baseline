"""
QUESTION:
Create a function `generate_fibonacci_series(num)` that generates the Fibonacci series for a given number `num`. The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones. The function should return a list of the Fibonacci series up to the `num`-th number. The function should handle cases where `num` is less than or equal to 0, and it should have a time complexity of O(n), where n is the given number.
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