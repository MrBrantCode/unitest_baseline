"""
QUESTION:
Create a function named `generate_fibonacci_series` that generates a series of Fibonacci numbers up to a given number of items (`num_items`) and calculates the sum of all the even Fibonacci numbers in the series. The function should return the series and the sum of even numbers.
"""

def generate_fibonacci_series(num_items):
    series = [0, 1]
    while len(series) < num_items:
        next_number = series[-1] + series[-2]
        series.append(next_number)
    even_numbers = [num for num in series if num % 2 == 0]
    even_sum = sum(even_numbers)
    return series, even_sum