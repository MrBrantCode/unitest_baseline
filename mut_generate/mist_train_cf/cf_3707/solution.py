"""
QUESTION:
Write a function `sum_of_digits` that takes a list of integers as input and returns the sum of all digits of the maximum absolute value in the list. The function should not use any built-in functions or libraries for arithmetic operations or string manipulations, and it should have a time complexity of O(log n), where n is the maximum absolute value among the given integers.
"""

def sum_of_digits(numbers):
    total_sum = 0
    max_value = 0
    
    # Find the maximum value among the given integers
    for num in numbers:
        abs_num = abs(num)
        if abs_num > max_value:
            max_value = abs_num
    
    # Calculate the sum of digits
    while max_value != 0:
        total_sum += max_value % 10
        max_value //= 10
    
    return total_sum