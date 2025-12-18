"""
QUESTION:
Write a function `sum_if_conditions_met` that takes two integers as input and returns their sum if both numbers are positive, the sum is greater than 15, and the sum is divisible by 3. If the conditions are not met, the function should return nothing or a default value.
"""

def sum_if_conditions_met(a, b):
    sum = a + b
    if a > 0 and b > 0 and sum > 15 and sum % 3 == 0:
        return sum