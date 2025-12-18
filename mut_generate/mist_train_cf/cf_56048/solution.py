"""
QUESTION:
Write a function named `exchange_with_floats_and_sci_notation` that takes two lists of numbers `lst1` and `lst2` as input, and returns "YES" if after swapping adjacent even and odd numbers, `lst1` contains all even numbers and `lst2` contains all odd numbers, otherwise return "NO".
"""

from decimal import Decimal

def exchange_with_floats_and_sci_notation(lst1, lst2):
    lst1 = [Decimal(str(n)) for n in lst1]
    lst2 = [Decimal(str(n)) for n in lst2]

    for i in range(len(lst1)):
        n1 = round(lst1[i])
        n2 = round(lst2[i])

        if (n1 % 2 == 0 and n2 % 2 == 0) or (n1 % 2 == 1 and n2 % 2 == 1):
            continue

        lst1[i], lst2[i] = lst2[i], lst1[i]

    for i in range(len(lst1)):
        if round(lst1[i]) % 2 == 1 or round(lst2[i]) % 2 == 0:
            return "NO"

    return "YES"