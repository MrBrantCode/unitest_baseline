"""
QUESTION:
Write a function `sum_divisible_by_five` that takes a list of integers as input and returns `True` if the sum of any two distinct numbers in the list is evenly divisible by five, and `False` otherwise. The function should check all possible pairs of distinct numbers in the list.
"""

def sum_divisible_by_five(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) % 5 == 0:
                return True

    return False