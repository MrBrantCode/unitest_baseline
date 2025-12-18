"""
QUESTION:
Create a function `largest_smallest_integers` that takes a list of integers as input. The function should return a tuple of four values: the largest negative even integer, the smallest non-negative even integer, the largest negative odd integer, and the smallest non-negative odd integer. If any of these criteria are not met (i.e., there are no integers that satisfy the condition), the corresponding value in the tuple should be `None`.
"""

def largest_smallest_integers(lst):
    max_neg_even = max_neg_odd = min_non_neg_even = min_non_neg_odd = None

    for num in lst:
        if num % 2 == 0:  # num is even
            if num >= 0:  # num is non-negative
                if min_non_neg_even is None or num < min_non_neg_even:
                    min_non_neg_even = num
            else:  # num is negative
                if max_neg_even is None or num > max_neg_even:
                    max_neg_even = num
        else:  # num is odd
            if num >= 0:  # num is non-negative
                if min_non_neg_odd is None or num < min_non_neg_odd:
                    min_non_neg_odd = num
            else:  # num is negative
                if max_neg_odd is None or num > max_neg_odd:
                    max_neg_odd = num

    return max_neg_even, min_non_neg_even, max_neg_odd, min_non_neg_odd