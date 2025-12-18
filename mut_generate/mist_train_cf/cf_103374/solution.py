"""
QUESTION:
Write a function named `find_powers_of_two` that takes two parameters `start` and `end` to find all powers of two within a given range `[start, end]` and returns them as a list. The function should be optimized for time complexity.
"""

def find_powers_of_two(start, end):
    powers_of_two = []
    power = 1

    while power <= end:
        if power >= start:
            powers_of_two.append(power)
        power = power << 1

    return powers_of_two