"""
QUESTION:
Create a function named `fibonacci_series` that takes an integer `n` as input, generates the Fibonacci series up to the given number `n`, and returns or prints the series along with the sum of the numbers in the series. The Fibonacci series should be generated without using any built-in functions or external libraries. The input `n` should be used as an upper limit for the series, meaning the series should not include numbers greater than `n`.
"""

def fibonacci_series(n):
    series = [0, 1]  # Initialize the series with the first two numbers
    sum_of_series = 1  # Initialize the sum with the first number
    
    # Generate the Fibonacci series
    while series[-1] < n:
        next_number = series[-1] + series[-2]
        if next_number <= n:
            series.append(next_number)
            sum_of_series += next_number
        else:
            break
    
    # Return the Fibonacci series and its sum
    return series, sum_of_series