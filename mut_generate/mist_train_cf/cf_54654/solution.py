"""
QUESTION:
Write a function `has_even_product(lst)` that determines if the multiplication of any three unique integers in a given list `lst` is an even number. The list `lst` will have a length of 3 <= n <= 10^3 and contain integers in the range of -10^6 <= ai <= 10^6.
"""

def has_even_product(lst):
    for num in lst:
        if num % 2 == 0:
            return True
    return False