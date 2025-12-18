"""
QUESTION:
Create a function `median(l: list, cmp_func: callable)` that calculates the median of a list `l` without sorting the list or using built-in sorting functions. The function should be able to handle lists with an even or odd number of elements, duplicates, and different data types. The `cmp_func` parameter is a custom comparison function that allows for flexible comparisons. If the median cannot be calculated due to mismatched data types, the function should return `None`.
"""

def median(l: list, cmp_func: callable):
    # Get list length
    l_len = len(l)

    # Raise error for empty list
    if l_len == 0: 
        return None

    # Create count of less than and greater than for each element
    counts = [(sum(1 for j in l if cmp_func(i, j) > 0),
               sum(1 for j in l if cmp_func(i, j) < 0)) for i in l]

    # Try to calculate median
    try:
        # For odd-sized lists, find the element where counts equal (n-1)//2
        if l_len % 2 == 1:
            return next(l[i] for i in range(l_len) if max(counts[i]) == (l_len - 1 )// 2)
        else:
            # For even-sized lists, find two elements where upper count equals n//2 and lower equals n//2 -1
            lo = next(l[i] for i in range(l_len) if counts[i][1] == l_len//2 - 1 and counts[i][0] <= l_len//2)
            hi = next(l[i] for i in range(l_len) if counts[i][1] <= l_len//2 and counts[i][0] == l_len//2 - 1)
            # Return average of two elements
            return (lo+hi)/2
    except StopIteration:
        # Return None if no median can be found (due to mismatched datatypes in cmp_func)
        return None