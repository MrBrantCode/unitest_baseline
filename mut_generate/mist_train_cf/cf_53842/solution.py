"""
QUESTION:
Create a function called `complex_median` that takes a list `l` of heterogeneous elements as input, where the list can contain integers, floats, strings, and tuples of any length. The function should calculate the median of all the elements in the list, treating tuples as a collection of individual elements. The length of a tuple is used to determine whether it is considered "even" or "odd", regardless of the values it contains. The function should not use any built-in or third-party library functions for sorting or calculating the median. Note that the function may need to convert strings to numbers and combine the elements of tuples into the list.
"""

def complex_median(l: list):
    even = []
    odd = []

    for item in l:
        if isinstance(item, (int, float)):
            if item % 2 == 0:  
                even.append(item)
            else:  
                odd.append(item)
        elif isinstance(item, str):
            if float(item) % 2 == 0:  
                even.append(float(item))
            else:  
                odd.append(float(item))
        elif isinstance(item, tuple):
            if len(item) % 2 == 0:  
                even.extend(item)
            else:  
                odd.extend(item)

    combined = sorted(odd + even)
    len_combined = len(combined)

    if len_combined % 2 == 0:
        median = (combined[len_combined//2] + combined[len_combined//2 - 1]) / 2
    else:
        median = combined[len_combined//2]

    return median