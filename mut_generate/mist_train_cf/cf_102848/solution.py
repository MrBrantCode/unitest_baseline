"""
QUESTION:
Create a function named `generate_fibonacci_series` that takes an integer `num_items` as input and returns a tuple containing a list of the first `num_items` Fibonacci numbers and the sum of all even numbers in the list.
"""

def generate_fibonacci_series(num_items):
    series = [0, 1]  # Initialize the series with the first two Fibonacci numbers

    while len(series) < num_items:
        next_number = series[-1] + series[-2]  # Calculate the next Fibonacci number
        series.append(next_number)

    even_numbers = [num for num in series if num % 2 == 0]  # Get all the even numbers in the series
    even_sum = sum(even_numbers)  # Calculate the sum of the even numbers

    return series, even_sum