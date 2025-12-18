"""
QUESTION:
Given an odd prime number p, arrange the numbers 1 through p-1 into (p-1)/2 pairs such that each number is used only once and the sum of the costs of all pairs, where the cost of each pair (a, b) is ab mod p, is minimized. Write a function `min_cost_product` that calculates the product of the costs of all pairs in an optimal pairing for a given p. The function should only take the odd prime number p as input and return the product of the costs of all pairs. The function should not take any other inputs and should not output any other values.
"""

def min_cost_product(p):
    """
    This function calculates the product of the costs of all pairs in an optimal pairing 
    for a given odd prime number p.

    Args:
    p (int): An odd prime number.

    Returns:
    int: The product of the costs of all pairs.
    """
    pairings = [(a, p - a) for a in range(1, p // 2 + 1)]
    total_cost = 1
    for (a, b) in pairings:
        total_cost *= (a * b) % p
    return total_cost