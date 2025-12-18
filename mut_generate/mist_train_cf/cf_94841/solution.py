"""
QUESTION:
Implement a function called `has_even_sum` that takes a list of positive integers as input and returns True if the sum of all the numbers in the list is even, and False otherwise. You are not allowed to use any built-in functions or methods for checking if a number is even. Assume the input list will always contain at least one element.
"""

def has_even_sum(numbers):
    def is_even(number):
        if number == 0:
            return True
        elif number == 1:
            return False
        else:
            return is_even(number - 2)
    
    def sum_numbers(numbers):
        if not numbers:
            return 0
        else:
            return numbers[0] + sum_numbers(numbers[1:])
    
    total_sum = sum_numbers(numbers)
    return is_even(total_sum)