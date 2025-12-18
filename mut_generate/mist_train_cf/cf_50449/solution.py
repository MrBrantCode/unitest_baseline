"""
QUESTION:
Create a function `fifth_root(numbers)` that calculates the fifth root of each number in a given list of numbers and returns the results as a list. The function should round the calculated fifth roots to 6 decimal places. The function should work for a list of numbers ranging from 10,000 to 50,000. The calculated fifth roots should be verified by checking if the fifth power of the root equals the original number, allowing for minor discrepancies due to floating point arithmetic.
"""

def fifth_root(numbers):
    return [round(number ** (1 / 5), 6) for number in numbers]