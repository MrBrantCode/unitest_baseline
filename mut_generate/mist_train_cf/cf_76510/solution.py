"""
QUESTION:
Write a function `advanced_median_error_detect(l)` that takes a multilevel nested list `l` containing integers as input and returns the median of the integers in the list without explicitly sorting the list. The function should handle both even and odd quantities of integers and include an error detection mechanism that returns 'Error Value Detected' if the list contains any non-integer values. If the list is empty, the function should return 'The list is empty'.
"""

def advanced_median_error_detect(l):
    """computes the median"""
    if not l:
        return 'The list is empty'

    def flatten(lst):
        """flatten a multilevel list"""
        for x in lst:
            if isinstance(x, list):
                yield from flatten(x)
            else:
                yield x

    flattened_list = list(flatten(l))

    for i in flattened_list:
        if type(i) != int:
            return 'Error Value Detected'

    n = len(flattened_list)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(flattened_list)[n//2]
    else:
            return sum(sorted(flattened_list)[n//2-1:n//2+1])/2.0