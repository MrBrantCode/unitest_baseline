"""
QUESTION:
Write a function `complex_median` that calculates the median of a list of elements regardless of their type or the list's order. The function should handle lists with an even or odd number of elements and ignore non-numerical types. If the list contains string numbers, it should be converted to actual numbers if possible. If no numbers are available, the function should raise an exception. The function should not sort the list.
"""

def complex_median(lst):
    """
    Compute the median of elements in the list regardless of their type or the list's order, 
    properly handling lists with an even or odd number of elements.
    """

    # Filter non-numerical types
    lst = [x for x in lst if type(x) in (int, float, str)]
    
    # Convert string numbers to actual numbers if possible
    for i in range(len(lst)):
        if type(lst[i]) == str:
            try:
                lst[i] = float(lst[i])  
            # a number string can always be converted to float
            except ValueError:
                pass  
    
    # Filter non-numerical types again because some strings may not be convertible to a number
    lst = [x for x in lst if type(x) in (int, float)]
    
    n = len(lst)
    if n == 0:
        raise Exception('No numbers available to calculate the median')

    # Calculate and return the median without sorting
    lst_sum = sum(lst)
    avg = lst_sum / n
    dists = [(x, abs(x - avg)) for x in lst]
    median = min(dists, key=lambda x: x[1])[0]
    
    return median