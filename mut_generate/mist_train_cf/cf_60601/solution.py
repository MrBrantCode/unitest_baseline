"""
QUESTION:
Write a function named `complex_median` that takes a list of complex or real numbers as input and returns the median of the list. If the input is not a list, return `None`. The function should handle both even and odd length lists, and it should convert complex numbers to their median and return the result as a complex number if necessary.
"""

def complex_median(lst):
    if not isinstance(lst, list):
        return None

    sortable_values = []
    for item in lst:
        if isinstance(item, complex):
            sortable_values.append((item.real, item.imag))
        else:
            sortable_values.append((item,))

    sortable_values.sort()

    n = len(sortable_values)
    if n % 2 == 1:
        median_tuple = sortable_values[n // 2]
    else:
        median_tuple1 = sortable_values[n // 2 - 1]
        median_tuple2 = sortable_values[n // 2]
        median_real_component = (median_tuple1[0] + median_tuple2[0]) / 2
        median_imag_component = ((median_tuple1[1:] or [0])[0] + (median_tuple2[1:] or [0])[0]) / 2
        median_tuple = (median_real_component, median_imag_component)

    if len(median_tuple) == 1:
        return median_tuple[0]
    else:
        return median_tuple[0] + median_tuple[1] * 1j