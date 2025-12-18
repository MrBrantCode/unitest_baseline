"""
QUESTION:
Write a function `median(lst, cmp_func)` that calculates the median of a list `lst` using a custom comparison function `cmp_func`. The function should return `None` if the input list is empty or if the median cannot be found due to mismatched data types in `cmp_func`. The function `cmp_func` is a comparator function that receives two parameters and returns a positive number if the first parameter is larger, 0 if they are the same, and a negative number otherwise.
"""

def median(lst: list, cmp_func: callable):
    # Get list length
    lst_len = len(lst)

    # Raise error for empty list
    if lst_len == 0: 
        return None

    # Create count of less than and greater than for each element
    counts = [(sum(1 for j in lst if cmp_func(i, j) > 0),
               sum(1 for j in lst if cmp_func(i, j) < 0)) for i in lst]

    # Try to calculate median
    try:
        # For odd-sized lists, find the element where counts equal (n-1)//2
        if lst_len % 2 == 1:
            return next(lst[i] for i in range(lst_len) if max(counts[i]) == (lst_len - 1) // 2)
        else:
            # For even-sized lists, find two elements where upper count equals n//2 and lower equals n//2 -1
            lo = next(lst[i] for i in range(lst_len) if counts[i][1] == lst_len//2 - 1 and counts[i][0] == lst_len//2)
            hi = next(lst[i] for i in range(lst_len) if counts[i][1] == lst_len//2 and counts[i][0] == lst_len//2 - 1)
            # Return average of two elements
            return (lo + hi) / 2
    except StopIteration:
        # Return None if no median can be found (due to mismatched data types in cmp_func)
        return None