"""
QUESTION:
Design a function called `sum_of_cubes` that takes a parameter which can be a positive integer or a string representing a positive integer and returns the sum of the cubes of its digits. The input parameter can have a maximum of 10^6 digits, can have leading zeros, and can contain any character from '0' to '9'.
"""

def sum_of_cubes(num):
    num = str(int(num))
    sum = 0
    for digit in num:
        sum += int(digit) ** 3
    return sum