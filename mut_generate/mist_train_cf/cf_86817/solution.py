"""
QUESTION:
Create a function named `generate_fibonacci_series` that takes an integer `num` as input and returns the Fibonacci series up to the nth number, where each number is the sum of the two preceding ones. The function should also modify the Fibonacci series by multiplying by 2 if the number is divisible by 2, dividing by 3 if the number is divisible by 3, and subtracting 5 if the number is divisible by 5, but only after the original number has been added to the series. The function should return an empty list if `num` is less than or equal to 0.
"""

def generate_fibonacci_series(num):
    a, b = 0, 1
    fib_series = []

    if num <= 0:
        return fib_series

    if num == 1:
        fib_series.append(0)
        return fib_series

    if num == 2:
        fib_series.extend([0, 1])
        return fib_series

    fib_series.extend([0, 1])

    for i in range(2, num):
        next_num = a + b
        a, b = b, next_num

        fib_series.append(next_num)

        if next_num % 2 == 0:
            fib_series.append(next_num * 2)

        if next_num % 3 == 0:
            fib_series.append(next_num // 3)

        if next_num % 5 == 0:
            fib_series.append(next_num - 5)

    return fib_series