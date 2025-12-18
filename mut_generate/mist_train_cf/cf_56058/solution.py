"""
QUESTION:
Define a function `nonagonal_numbers(start, end=None)` that takes either a positive integer, an array of positive integers, or a range as input and returns a tuple of nonagonal numbers, their cumulative sums, and their products.

The nonagonal numbers are a sequence of numbers where each term is calculated as `m * (7 * m - 5) // 2` for `m` in the range 1 to 1000. The cumulative sums and products are calculated based on these nonagonal numbers.

The function should perform input validation to ensure that the input is valid, and return an error message if the input is not a positive integer, an array of positive integers, or a range. If the input is a range, the function should return the nonagonal numbers, cumulative sums, and products for the specified range. If the input is a list of numbers, the function should return the nonagonal numbers, total sum, and total product for the specified numbers.
"""

def nonagonal_numbers(start, end=None):
    # Define a list of nonagonal numbers & precalculate the values for 1 to 1000
    nonagonals = [0]
    for m in range(1, 1001):
        nonagonals.append(m * (7 * m - 5) // 2)

    # Define a list of their cumulative sums
    sums = [0]
    for n in range(1, 1001):
        sums.append(sums[-1] + nonagonals[n])

    # And a list of their products as well (with an initial value of 1 for multiplication)
    products = [1]
    for n in range(1, 1001):
        products.append(products[-1] * nonagonals[n])

    # Input verification
    if not isinstance(start, (int, list, range)):
        return "Please provide either a positive integer, an array of positive integers or a range."
    if isinstance(start, int) and start < 1:
        return "Please provide a positive integer."
    if isinstance(start, list) and not all([isinstance(u, int) and u > 0 for u in start]):
        return "Array should contain only positive integers."
    if isinstance(start, range) and (start.start < 1 or start.step != 1 or start.stop < start.start):
        return "Invalid range."
    if end and (not isinstance(end, int) or end < start):
        return "Invalid end of range."

    if isinstance(start, int):
        if end:
            return nonagonals[start:end+1], sums[end], products[end]
        else:
            return nonagonals[start], sums[start], products[start]
    elif isinstance(start, range):
        start = list(start)
        nonags = [nonagonals[v] for v in start]
        total_sum = sum([sums[v] for v in start])
        total_product = 1
        for v in start:
            total_product *= products[v]
        return nonags, total_sum, total_product
    else: # start is a list of numbers
        nonags = [nonagonals[v] for v in start]
        total_sum = sum([sums[v] for v in start])
        total_product = 1
        for v in start:
            total_product *= products[v]
        return nonags, total_sum, total_product