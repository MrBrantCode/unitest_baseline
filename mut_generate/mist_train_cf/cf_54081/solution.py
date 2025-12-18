"""
QUESTION:
Write a function `swap_for_odds(lst1, lst2)` that takes two non-empty lists of integers as input and returns "YES" if it's possible to transform `lst1` into a list of only odd numbers by swapping elements with `lst2` while keeping the total sum of elements constant, and "NO" otherwise.
"""

def swap_for_odds(lst1, lst2):
    sum_lst1 = sum(lst1)
    sum_lst2 = sum(lst2)

    if (sum_lst1 + sum_lst2) % 2 != 0:
        return "NO"

    has_odd_lst1 = any(i % 2 != 0 for i in lst1)
    has_even_lst2 = any(i % 2 == 0 for i in lst2)

    return "YES" if has_odd_lst1 and has_even_lst2 else "NO"