"""
QUESTION:
Write a function named `find_highest_common_factor` that takes two positive integers `a` and `b` as input, where `a` and `b` are not equal to each other and are within the range of 1 to 1000. The function should return the highest common factor of `a` and `b`. The function should be able to handle cases where `a` and `b` are very large (up to 10^12) efficiently.
"""

def find_highest_common_factor(a, b):
    if a == 1 or b == 1:
        return 1

    highest_common_factor = 1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            highest_common_factor = i

    return highest_common_factor