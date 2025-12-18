"""
QUESTION:
Create a generator expression function `squared_values_not_divisible_by_three` that takes a list of numbers as input and returns the squared values of the numbers that are not divisible by 3. The function should exclude any numbers that are divisible by 3.
"""

def squared_values_not_divisible_by_three(list_of_nums):
    return (num**2 for num in list_of_nums if num % 3 != 0)