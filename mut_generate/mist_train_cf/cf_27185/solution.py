"""
QUESTION:
Implement the function `optimal_sieve(d, expected_cost)` that returns the optimal parameters `(a, b)` for the sieve algorithm given the range `d` and the expected cost, considering the cost factors `K_COST` and `K_FILTER_COST`. The cost of the sieve algorithm is calculated using the formula: `cost = K_COST * d + K_FILTER_COST * sieve`, where `sieve` is the number of elements remaining after sieving. The function should return the optimal parameters as a tuple `(a, b)` where `a` and `b` are integers representing the parameters for the sieve algorithm.
"""

def optimal_sieve(d, expected_cost, K_COST, K_FILTER_COST):
    non_trivial_a_b = d * 23  # removes 2, 3, 5, ...
    sieve = d - non_trivial_a_b
    b = int(expected_cost / (K_COST * d + K_FILTER_COST * sieve))
    a = non_trivial_a_b + b
    return a, b