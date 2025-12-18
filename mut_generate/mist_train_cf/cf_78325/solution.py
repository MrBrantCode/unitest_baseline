"""
QUESTION:
Construct a function `geometric_series` that takes three parameters: `start`, `ratio`, and `length`, representing the starting number, the common ratio, and the number of terms in a geometric series, respectively. The function should generate a geometric series with the given parameters, ensure that each number in the series is unique, and return a sorted list of unique numbers.
"""

def geometric_series(start, ratio, length):
    series = [start]

    for _ in range(1, length):
        series.append(series[-1] * ratio)

    unique_series = set(series)
    return sorted(list(unique_series))