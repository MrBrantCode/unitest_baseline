"""
QUESTION:
Create a function called `fibonacci` that takes a list of integers `n` as input, representing the positions of the Fibonacci sequence to be calculated. The function should return a list of integers corresponding to the Fibonacci numbers at the specified positions. The input list `n` can contain non-contiguous positions, and the positions can be up to 10,000. The function should be able to handle large Fibonacci numbers efficiently.
"""

def fibonacci(n):
    fib_series = [0, 1]

    # Calculate the Fibonacci sequence up to the largest number in the input list
    for i in range(2, max(n)+1):
        fib_series.append(fib_series[i-1] + fib_series[i-2])

    # Return the Fibonacci numbers corresponding to the input list
    return [fib_series[i] for i in n]