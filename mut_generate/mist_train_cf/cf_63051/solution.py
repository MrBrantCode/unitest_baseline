"""
QUESTION:
Create a function `monotonic_extended(l: list, strict: bool = False, ignore_negative: bool = False, ignore_zero: bool = False)` that checks if the numerical array adheres to a monotonically ascending or descending pattern. The function should consider the parameters 'strict', 'ignore_negative', and 'ignore_zero'. If 'strict' is True, consecutive elements must not be the same; otherwise, they can be equal. If 'ignore_negative' is True, negative numbers are not considered. If 'ignore_zero' is True, zeroes in the list are not considered.
"""

def monotonic_extended(l: list, strict: bool = False, ignore_negative: bool = False, ignore_zero: bool = False):
    """
    This function checks if the numerical array adheres to a monotonically ascending or descending pattern, considering the strictness and ignore_negative parameter. If strict is set to True, consecutive elements must not be the same; otherwise, they can be equal. If ignore_negative is True, negative numbers are not considered. If ignore_zero is True, zeroes in the list will not be considered.
    """

    if ignore_negative:
        l = [i for i in l if i >= 0]

    if ignore_zero:
        l = [i for i in l if i != 0]
    
    if strict:
        return all(i < j for i, j in zip(l, l[1:])) or all(i > j for i, j in zip(l, l[1:]))
    else:
        return all(i <= j for i, j in zip(l, l[1:])) or all(i >= j for i, j in zip(l, l[1:]))