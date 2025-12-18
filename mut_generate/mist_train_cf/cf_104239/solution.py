"""
QUESTION:
Create a function named `fibonacci_sum` that calculates and returns the sum of the first `n` Fibonacci numbers, where `n` is a positive integer passed as an argument to the function, and the function should handle `n` greater than or equal to 2.
"""

def fibonacci_sum(n):
    fib_nums = [0, 1]  # List to store Fibonacci numbers
    sum_fib = 1  # Initialize sum of Fibonacci numbers
    for i in range(2, n):
        fib_num = fib_nums[i-1] + fib_nums[i-2]  # Calculate the next Fibonacci number
        fib_nums.append(fib_num)  # Add the Fibonacci number to the list
        sum_fib += fib_num  # Add the Fibonacci number to the sum
    return sum_fib