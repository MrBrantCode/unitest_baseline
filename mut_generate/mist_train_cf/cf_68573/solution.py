"""
QUESTION:
Design a function `fibonacci_and_golden_ratio` that generates the first 'n' Fibonacci numbers and their corresponding Golden Ratio approximations. The function should be optimized for speed and efficient calculation for large 'n'. It should return two lists: the first containing the Fibonacci numbers and the second containing the Golden Ratio approximations for each pair of consecutive Fibonacci numbers. The Golden Ratio for the first two Fibonacci numbers should be "N/A" due to division by zero.
"""

def fibonacci_and_golden_ratio(n):
    if n == 1:
        fib_nums = [0]
        ratios = ["N/A"]
    elif n == 2:
        fib_nums = [0, 1]
        ratios = ["N/A", "N/A"]
    else:
        fib_nums = [0, 1]
        ratios = ["N/A", "N/A"]
        for _ in range(2, n):
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
            ratios.append(fib_nums[-1] / fib_nums[-2])
    return fib_nums, ratios