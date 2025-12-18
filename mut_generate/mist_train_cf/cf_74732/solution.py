"""
QUESTION:
Write a function called `triples_sum_to_zero` that takes a list of integers as input and returns `True` if it contains at least three unique elements that sum to zero, and `False` otherwise. The function should handle lists of any size and content.
"""

def triples_sum_to_zero(lst):
    n = len(lst)
    if n < 3:
        return False
    lst.sort()
    for i in range(n - 1):
        a = lst[i]
        start = i + 1
        end = n - 1
        while start < end:
            if a + lst[start] + lst[end] == 0:
                return True
            elif a + lst[start] + lst[end] < 0:
                start += 1
            else:
                end -= 1
    return False