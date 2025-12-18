"""
QUESTION:
Given a non-negative number, return the next bigger polydivisible number, or an empty value like `null` or `Nothing`.

A number is polydivisible if its first digit is cleanly divisible by `1`, its first two digits by `2`, its first three by `3`, and so on. There are finitely many polydivisible numbers.
"""

def find_next_polydivisible(n):
    # Precompute the list of polydivisible numbers
    (d, polydivisible, arr) = (1, [], list(range(1, 10)))
    while arr:
        d += 1
        polydivisible.extend(arr)
        arr = [n for x in arr for n in range(-(-x * 10 // d) * d, (x + 1) * 10, d)]
    
    # Use binary search to find the next polydivisible number
    from bisect import bisect
    idx = bisect(polydivisible, n)
    
    # Return the next polydivisible number if it exists
    if idx < len(polydivisible):
        return polydivisible[idx]
    else:
        return None