"""
QUESTION:
Implement a function `longest_recurring_cycle` that takes an integer n as input and returns the value of d less than n for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def longest_recurring_cycle(n: int) -> int:
    def recurring_cycle_length(denominator):
        remainders = {}
        remainder = 1 % denominator
        position = 0
        while remainder not in remainders and remainder != 0:
            remainders[remainder] = position
            remainder = (remainder * 10) % denominator
            position += 1
        return position - remainders.get(remainder, 0)

    max_cycle_length = 0
    result = 0
    for d in range(2, n):
        cycle_length = recurring_cycle_length(d)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            result = d
    return result