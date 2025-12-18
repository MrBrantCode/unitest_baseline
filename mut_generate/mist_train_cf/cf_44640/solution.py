"""
QUESTION:
Implement a function `calculate_product(lst)` that calculates the product of all integers in a list `lst` and uses memoization to optimize subsequent product calculations of the same list. The function should return the product of the list and store the result in a memoization dictionary for future use. Note that the input list is assumed to be unchanged between function calls.
"""

def calculate_product(lst, memo={}):
    # Convert list to tuple for it to be hashable
    lst_tuple = tuple(lst)
    
    # Check if product of this tuple is already calculated
    if lst_tuple in memo:
        return memo[lst_tuple]

    prod = 1
    for num in lst:
        prod *= num

    # Save product to memo
    memo[lst_tuple] = prod
    return prod