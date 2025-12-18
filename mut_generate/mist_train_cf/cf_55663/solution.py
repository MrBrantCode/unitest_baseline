"""
QUESTION:
Create a function named `calculate_power_and_sum_of_squares(n)` that calculates the result of raising 2 to the power of `n` and the sum of the squares of 2 raised to different powers from 2 to `n` (inclusive), where 2 ≤ `n` ≤ 10. The function should return both results and optimize the calculations with minimal iterations.
"""

def calculate_power_and_sum_of_squares(n):
    # Check If the Value Is within the Acceptable Range
    if n < 2 or n > 10:
        return "Number out of range. Please enter a number between 2 and 10."

    # Initialize Variables
    power_of_two = 2 ** n
    sum_of_squares = 0

    # Iterate to Calculate the Sum of Squares
    for i in range(2,n+1):
        sum_of_squares += (2 ** i) ** 2

    # Return the Results
    return power_of_two, sum_of_squares