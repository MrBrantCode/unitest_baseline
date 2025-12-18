"""
QUESTION:
Create a function `sum_of_squares_is_prime_in_ranges(lists, ranges)` that takes in two lists: `lists`, a list of lists of integers, and `ranges`, a list of tuples representing inclusive ranges. The function should return a tuple of boolean values, where each value corresponds to a list in `lists` and indicates whether the sum of squares of its elements is a prime number and lies within the corresponding range in `ranges`. Assume the length of `lists` and `ranges` is the same.
"""

def is_prime(n):
    """Check if number n is a prime number."""
    if n == 1 or (n % 2 == 0 and n > 2): 
        return False
    for current in range(3, int(n ** 0.5) + 1, 2):
        if n % current == 0: 
            return False
    return True

def in_range(n, range_tuple):
    """Check if number n falls within the specified range (inclusive)."""
    return range_tuple[0] <= n <= range_tuple[1]

def sum_of_squares_is_prime_in_ranges(lists, ranges):
    """Check if the sum of squares of each list is a prime number and lies within the corresponding range."""
    result = []
    for l, r in zip(lists, ranges):
        sum_of_squares = sum(i**2 for i in l)
        result.append(is_prime(sum_of_squares) and in_range(sum_of_squares, r))
    return tuple(result)