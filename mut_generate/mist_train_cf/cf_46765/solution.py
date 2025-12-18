"""
QUESTION:
Write a function `will_it_fly(a, b, m, n)` that checks whether a given list `a` of integers can achieve flight. The list `a` needs to meet four requirements to fly: it must be palindromic (symmetric), the total integer value within the list must be less than or equal to `b`, the total of every alternate integer must be less than or equal to `m`, and the total of the remaining integers must be less than or equal to `n`. The function should return `True` if the list can fly and `False` otherwise.
"""

def will_it_fly(a, b, m, n):
    total = 0
    alt_sum_1 = 0
    alt_sum_2 = 0
    length = len(a)
    # checking if the list is palindromic
    if a != a[::-1]:
        return False
    for i in range(length):
        total += a[i]
        # calculate sum of alternate integers 
        if i%2 == 0:
            alt_sum_1 += a[i]
        else:
            alt_sum_2 += a[i]
    # check the constraints
    if total > b or alt_sum_1 > m or alt_sum_2 > n:
        return False
    return True