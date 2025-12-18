"""
QUESTION:
Implement a function `largest_smallest_summed_integers` that takes a list of integers as input and returns a tuple (a, b, c, d, e, f). The values a, b, c, and d represent the maximum negative even integer, least positive even integer, maximum negative odd integer, and least positive odd integer from the input list respectively. If any of these integers do not exist, they should be replaced with `None`. The value e is the sum of a, b, c, and d, treating `None` as 0 in the sum. The value f is the sum of a, b, c, d, and e.
"""

def largest_smallest_summed_integers(lst):
    # filtering the list into even and odd numbers
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    # finding the maximum of negative numbers and minimum of positive numbers
    a = max([x for x in evens if x < 0], default=None)
    b = min([x for x in evens if x > 0], default=None)
    c = max([x for x in odds if x < 0], default=None)
    d = min([x for x in odds if x > 0], default=None)
    # calculating the sum 'e' and 'f'
    e = (a if a else 0) + (b if b else 0) + (c if c else 0) + (d if d else 0)
    f = e + (e if e else 0)
    return a, b, c, d, e, f