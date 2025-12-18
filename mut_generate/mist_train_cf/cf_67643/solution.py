"""
QUESTION:
Write a recursive function named `pell(n)` to calculate the nth term of the Pell sequence, where each term is calculated as 2 times the previous term plus the term before the previous term. Use memoization to avoid redundant computation and calculate the first 40 elements of the sequence.
"""

# initialize a dictionary to memoize pell sequence values
pell_dict = {0: 0, 1: 1}

def entrance(n):
    # check if the value is already computed
    if n not in pell_dict:
        # calculate the nth term of the sequence
        pell_dict[n] = 2 * entrance(n-1) + entrance(n-2)
    return pell_dict[n]