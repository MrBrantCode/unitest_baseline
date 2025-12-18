"""
QUESTION:
Write a function called `sum_of_squares` that takes a list of integers as input and returns the sum of the squares of the digits for each number in the list. The input list should be between 1 and 100 elements long, and each number in the list should be between 1 and 10^9. The solution should have a time complexity of O(n), where n is the total number of digits in the input list.
"""

def sum_of_squares(num):
    return sum(int(digit)**2 for digit in str(num))