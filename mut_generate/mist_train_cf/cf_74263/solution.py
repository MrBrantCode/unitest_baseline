"""
QUESTION:
Create a function `generate_series` that takes two parameters, `N` and `X`, where `N` is a positive integer representing the term in the series to be determined, and `X` is an integer to be searched within the generated series. The function should generate a series of integers where each term is the sum of the preceding pair of even integers, starting from 2 and 4. The function should return the Nth term in the series, the entire series up to the Nth term in reverse order, and a boolean indicating whether `X` exists in the series.
"""

def generate_series(N, X):
    series = [2, 4]
    while len(series) < N:
        series.append(series[-1] + series[-2])

    nth_term = series[N - 1]
    reverse_order = series[::-1]
    is_in_series = X in series

    return nth_term, reverse_order, is_in_series