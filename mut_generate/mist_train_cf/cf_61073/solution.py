"""
QUESTION:
Write a function `divide_pairs(n, m)` that generates a list of tuples of the form `(x, y, n/x, m/y)` where `x` divides `n` and `y` divides `m`. The function should take two parameters `n` and `m` which are integers greater than or equal to 1, and return the list of tuples sorted by the product of the first and last elements and then by the product of the second and third elements in descending order. The values in the tuples must be integers.
"""

def divide_pairs(n, m):
    """Return a list of tuples of the form (x, y, n/x, m/y) where x divides n and y divides m."""
    divisors_n = [i for i in range(1, n+1) if n % i == 0]
    divisors_m = [i for i in range(1, m+1) if m % i == 0]
    result = [(x, y, n//x, m//y) for x in divisors_n for y in divisors_m]

    # sorting in descending order
    result.sort(key = lambda x: (x[0]*x[2], x[1]*x[3]), reverse=True)
    
    return result