"""
QUESTION:
Create a function named `find_multiples` that takes three parameters: `n`, `lower_limit`, and `upper_limit`, and returns a list of all multiples of `n` within the range from `lower_limit` to `upper_limit` (inclusive).
"""

def find_multiples(n, lower_limit, upper_limit):
    # Initialize an empty list for storing multiples
    multiples = []

    # Start from the lower limit
    # If the lower limit is less than n, start from n
    start = max(n, lower_limit)

    # Go through each number in the range
    for i in range(start, upper_limit+1):
        # Check if the number is a multiple of n
        if i % n == 0:
            multiples.append(i)

    return multiples