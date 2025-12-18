"""
QUESTION:
Create a function named `check(num)` that takes a single argument `num`. The function should return a string indicating whether the input number is even, prime, both, or neither. The function should also handle invalid inputs, which include non-integer and negative values. The output should be one of the following: "Even and Prime", "Even only", "Prime only", "Neither Even Nor Prime", or "Invalid input! Please enter a positive integer."
"""

def check(num):
    if not isinstance(num, int) or num < 0:
        return "Invalid input! Please enter a positive integer."
    if num == 2:
        return "Even and Prime"
    elif num % 2 == 0:
        return "Even only"
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return "Neither Even Nor Prime"
        return "Prime only"