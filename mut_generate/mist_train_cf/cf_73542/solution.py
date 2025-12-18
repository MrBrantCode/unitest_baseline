"""
QUESTION:
Write a function `series_aggregate` that takes two parameters: `n`, the number of terms in the series, and `type`, a string indicating whether the series consists of odd or even numbers. The function should return the sum of the first `n` terms of the series. If `type` is 'odd', the series should consist of numbers of the form `2n-1`. If `type` is 'even', the series should consist of numbers of the form `2n`. The function should be able to handle any positive integer value of `n` and should default to 'odd' if `type` is not provided.
"""

def series_aggregate(n, type='odd'):
    if type == 'odd':
        # Formula for the sum of an arithmetic series of odds: n^2
        return n**2
    else:
        # Formula for the sum of an arithmetic series of evens: n*(n+1)
        return n*(n+1)