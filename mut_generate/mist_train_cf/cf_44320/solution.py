"""
QUESTION:
Create a function complex_median that takes a list of mixed types (integers, strings, floating-point numbers) as input. The function should calculate the median of the numerical values in the list without sorting the list in any way. It should filter out non-numerical types, convert string numbers to actual numbers if possible, and handle lists with both even and odd number of elements. The function should return the median value.
"""

def complex_median(l: list):
    """Compute the median of elements in the list l regardless of their type or the list's order, properly handling tuples with an even or odd number of elements."""
    
    # Filter non-numerical types
    l = [x for x in l if type(x) in {int, float, str}]

    # Convert string numbers to actual numbers if possible
    for i in range(len(l)):
        if type(l[i]) == str:
            try:
                l[i] = float(l[i])  # a number string can always be converted to a float
            except ValueError:
                pass  # some strings may not be converted to a float, keep them as string

    # Filter non-numerical types again because some string may not be convertible to a number
    l = [x for x in l if type(x) in {int, float}]

    n = len(l)
    if n == 0:
        raise Exception('No numbers available to calculate the median')

    # Calculate and return the median without sorting
    l_sum = sum(l)
    avg = l_sum / n
    dists = [(x, abs(x - avg)) for x in l]
    median = min(dists, key=lambda x: x[1])[0]

    return median