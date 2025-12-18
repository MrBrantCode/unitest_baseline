"""
QUESTION:
Create a function `sum_of_fourth_powers` that takes two arguments: `n` and `start` (default is 1), to calculate the sum of the fourth powers of the first n natural numbers. The function should use a for loop, return an error message if `n` or `start` is not a positive integer or if `start` is larger than `n`, and print the output of each iteration displaying the value of the number being added and the running sum.
"""

def sum_of_fourth_powers(n, start=1):
    if not isinstance(n, int) or n < 1:
        return "n should be a positive integer"
    if not isinstance(start, int) or start > n:
        return "start should be an integer between 1 and n"
    result = 0
    for i in range(start, n+1):
        fourth_power = i ** 4
        result += fourth_power
        print(f"Adding {fourth_power}, Running Sum: {result}")
    return result