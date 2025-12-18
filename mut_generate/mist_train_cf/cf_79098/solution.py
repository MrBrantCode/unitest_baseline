"""
QUESTION:
Write a function `catalan_numbers(n)` that generates the nth element of the Catalan sequence, optimizing the calculation to efficiently handle large values of n. The function should return the nth Catalan number. The function should be optimized to reduce repeated calculations, ideally achieving a time complexity of O(n^2) or better.
"""

def catalan_numbers(n):
    """
    Generates the nth element of the Catalan sequence.

    Args:
    n (int): The index of the Catalan number to generate.

    Returns:
    int: The nth Catalan number.
    """
    
    # Base case: C(0) and C(1) are both 1
    if n == 0 or n == 1:
        return 1

    # Initialize an array to store Catalan numbers
    catalan = [0 for _ in range(n + 1)]
    
    # Base cases
    catalan[0] = 1
    catalan[1] = 1

    # Calculate each Catalan number iteratively
    for i in range(2, n + 1):
        for j in range(i):
            # Apply the recurrence relation: C(i) = sum(C(j) * C(i - j - 1))
            catalan[i] += catalan[j] * catalan[i - j - 1]

    # Return the nth Catalan number
    return catalan[n]