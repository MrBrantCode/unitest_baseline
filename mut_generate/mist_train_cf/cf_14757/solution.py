"""
QUESTION:
Generate a function called `lucas_series(n)` that generates the Lucas series up to the nth number. The Lucas series starts with 2 and 1, and each subsequent number is the sum of the two preceding numbers.
"""

def lucas_series(n):
    if n == 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 1]
    else:
        series = [2, 1]
        while len(series) < n:
            series.append(series[-1] + series[-2])
        return series