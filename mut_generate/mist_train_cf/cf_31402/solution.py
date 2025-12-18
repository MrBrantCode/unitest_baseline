"""
QUESTION:
Write a function `calculate_sum_of_replicated_integers(a)` that takes an integer `a` as input and calculates the sum of `a`, `aa`, and `aaa`, where `aa` and `aaa` are created by replicating the digits of `a`. For example, if `a` is 5, the function should return the sum of 5, 55, and 555.
"""

def calculate_sum_of_replicated_integers(a):
    n1 = int("%s" % a)
    n2 = int("%s%s" % (a, a))
    n3 = int("%s%s%s" % (a, a, a))
    return n1 + n2 + n3