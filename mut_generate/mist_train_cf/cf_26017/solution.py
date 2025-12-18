"""
QUESTION:
Write a function `appears_more_than_twice` that takes two input parameters: a list `lst` and a number `num`. The function should return `True` if `num` occurs more than twice in `lst`, otherwise return `False`.
"""

def appears_more_than_twice(lst, num):
    count = 0
    for n in lst:
        if n == num:
            count += 1
    return count > 2