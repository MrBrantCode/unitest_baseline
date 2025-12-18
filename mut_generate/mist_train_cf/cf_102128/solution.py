"""
QUESTION:
Create a function `check_divisibility` that takes an integer `num` as input. Check if `num` is divisible by both 3 and 5, or if it is negative and not divisible by either 3 or 5. Return a corresponding message for the conditions met.
"""

def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        return "The number is divisible by both 3 and 5."
    elif num < 0 and (num % 3 != 0 or num % 5 != 0):
        return "The number is negative and not divisible by either 3 or 5."
    else:
        return "The number does not meet the specified conditions."