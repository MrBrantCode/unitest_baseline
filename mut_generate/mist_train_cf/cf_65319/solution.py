"""
QUESTION:
Write a function called `sum_of_squares_of_n_odds` that takes an integer `n` as input, generates the first `n` odd numbers, calculates the square of each odd number, and returns the sum of these squares.
"""

def sum_of_squares_of_n_odds(n):
    # Step 1: Generate a list of the first n odd numbers.
    odd_numbers = [2 * i + 1 for i in range(n)]

    # Step 2: Calculate the square of each odd number in the list.
    squared_odd_numbers = [x ** 2 for x in odd_numbers]

    # Step 3: Sum the squared odd numbers.
    total_sum = sum(squared_odd_numbers)

    return total_sum