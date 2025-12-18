"""
QUESTION:
Create a function `sum_of_squares_is_prime_in_ranges(lists, ranges)` that takes two parameters: a list of integer lists (`lists`) and a list of integer ranges (`ranges`). The function should return a tuple where each element is a boolean indicating whether the sum of squares of elements in the corresponding list is within the corresponding range and is a prime number. The function assumes that the lengths of `lists` and `ranges` are equal.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_squares_is_prime_in_ranges(lists, ranges):
    return tuple(rng[0] <= sum(x**2 for x in lst) <= rng[1] and is_prime(sum(x**2 for x in lst)) for lst, rng in zip(lists, ranges))