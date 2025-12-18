"""
QUESTION:
Design a function `sum_of_cubes` that takes a parameter `num`, which can be a positive integer or a string representing a positive integer, and returns the sum of the cubes of its digits. The input can have a maximum of 10^6 digits and may contain leading zeros.
"""

def sum_of_cubes(num):
    num = str(int(num))
    sum = 0
    for digit in num:
        sum += int(digit) ** 3
    return sum