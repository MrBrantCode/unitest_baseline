"""
QUESTION:
Create a function `sum_of_even_numbers` that calculates the sum of all even numbers in a given list of integers. The function should take one argument, a list of integers, and return the sum of the even numbers in the list. The function should not include any input/output operations.
"""

def sum_of_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum