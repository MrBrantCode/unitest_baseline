"""
QUESTION:
Create a function `uniqueMinPath` that takes a 2D grid of prime numbers and an integer `k` as input. The grid is an NxN array where N ranges from 4 to 10, and the prime numbers range between 2 and N². The function should return an ascending sorted list of unique prime numbers in a chain of length `k` that starts from any cell and moves to its adjoining cells in a counter-clockwise spiral pattern, without going outside the array boundaries. If the chain length is less than `k` due to the repetition of prime numbers, the function should raise an exception.
"""

def uniqueMinPath(grid, k):
    """
    This function generates a list of unique prime numbers in a chain of length k 
    that starts from any cell and moves to its adjoining cells in a counter-clockwise 
    spiral pattern, without going outside the array boundaries.

    Args:
        grid (list): A 2D grid of prime numbers.
        k (int): The length of the chain.

    Returns:
        list: An ascending sorted list of unique prime numbers.

    Raises:
        Exception: If the chain length is less than k due to the repetition of prime numbers.
    """
    flattened_grid = [item for sublist in grid for item in sublist]
    flattened_grid.sort()
    unique_primes = []
    for num in flattened_grid:
        if len(unique_primes) == k:
            break
        if num not in unique_primes:
            unique_primes.append(num)
    if len(unique_primes) < k:
        raise Exception("Chain length less than k due to repetition of prime numbers")
    return unique_primes