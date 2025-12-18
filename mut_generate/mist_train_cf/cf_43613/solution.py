"""
QUESTION:
Implement a function `median` that calculates the median of a list of numbers. The function should take two parameters: `l`, a list of numbers, and `cmp_func`, a comparison function that takes two numbers as input and returns a value that determines their order. The function should first remove any duplicate entries from the list. If the length of the list is even, the function should return the average of the two middle numbers. If the length of the list is odd, the function should return the middle number.
"""

def median(l: list, cmp_func: callable):
    # Remove any duplicate entries for correctness purpose
    l = list(dict.fromkeys(l))

    # Get length of the list
    n = len(l)

    # Median calculation for even length lists
    if n % 2 == 0:
        left, right = None, None
        for i in l:
            less = len([j for j in l if cmp_func(j, i) < 0])
            equal = len([j for j in l if cmp_func(j, i) == 0])
            if less <= n // 2 - 1 < less + equal:
                left = i
            if less <= n // 2 < less + equal:
                right = i
                break

        return (left + right) / 2

    # Median calculation for odd length lists
    else:
        for i in l:
            less = len([j for j in l if cmp_func(j, i) < 0])
            equal = len([j for j in l if cmp_func(j, i) == 0])
            if less <= n // 2 < less + equal:
                return i