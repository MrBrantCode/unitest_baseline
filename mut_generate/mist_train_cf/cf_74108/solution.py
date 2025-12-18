"""
QUESTION:
Write a function `within_thresholds_and_harmonic_mean` that takes a list of integers `l` and two integer thresholds `t1` and `t2`. Return `True` if all integers in `l` are within the range `[t1, t2]` (inclusive) and print the harmonic mean of these integers. Otherwise, return `False`. The harmonic mean calculation should not use any built-in Python libraries.
"""

def within_thresholds_and_harmonic_mean(numbers, threshold1, threshold2):
    n = len(numbers)
    if all(threshold1 <= num <= threshold2 for num in numbers):
        reciprocal_sum = sum(1/num for num in numbers if num != 0)
        harmonic_mean = n / reciprocal_sum if reciprocal_sum != 0 else None
        print("Harmonic mean:", harmonic_mean)
        return True
    else:
        print("Not all numbers are within thresholds")
        return False