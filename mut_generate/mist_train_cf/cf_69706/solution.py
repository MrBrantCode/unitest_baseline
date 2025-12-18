"""
QUESTION:
Write a function called `generate_lucas_sequence(n)` that generates the first n Lucas numbers. The function should start the sequence with 2 and 1, and each subsequent number should be the sum of the two preceding numbers. The function must handle errors and edge cases gracefully, and be optimized for runtime speed. The input `n` should be a positive integer.
"""

def generate_lucas_sequence(n):
    # Check n is not less than 1
    if n < 1:
        return "Error: input must be an integer greater than 0"
    # Check input is integer
    elif not isinstance(n, int):
        return "Error: input must be an integer"
    else:
        # initialize base cases
        lucas = [2,1] + [0]*(n-2)
        # calculate Lucas numbers
        for i in range(2,n):
            lucas[i] = lucas[i-1] + lucas[i-2]
        return lucas[:n]