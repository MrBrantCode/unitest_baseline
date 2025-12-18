"""
QUESTION:
Write a function `nth_passenger_probability(n)` that calculates the probability that the last passenger will end up in their own seat when 'n' passengers are boarding an airplane with exactly 'n' seats. The function should take an integer 'n' as input, where 1 <= n <= 10^5, and return the probability as a decimal value.
"""

def nth_passenger_probability(n):
    """
    Calculate the probability that the last passenger will end up in their own seat 
    when 'n' passengers are boarding an airplane with exactly 'n' seats.

    Args:
    n (int): The number of passengers and seats, where 1 <= n <= 10^5.

    Returns:
    float: The probability as a decimal value.
    """
    if n == 1:
        return 1.0
    else:
        return 0.5