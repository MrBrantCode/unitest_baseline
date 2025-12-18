"""
QUESTION:
Write a function `numberOfSteps(num)` that takes a non-negative integer `num` as input and returns the number of steps to reduce it to zero. If the current number is even, it must be divided by 2, otherwise, it must be subtracted by 1. However, if the number is divisible by 3, subtract 2 from it instead of 1. The function should be able to handle inputs where `0 <= num <= 10^6`.
"""

def numberOfSteps(num):
    steps = 0
    while num != 0:
        if num % 3 == 0:
            num -= 2
        elif num % 2 == 0:
            num /= 2
        else:
            num -= 1
        steps += 1
    return steps