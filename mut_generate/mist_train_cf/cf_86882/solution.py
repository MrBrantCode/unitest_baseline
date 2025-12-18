"""
QUESTION:
Create a function `find_divisible_numbers(numbers)` that takes a list of integers as input, calculates the sum of all the numbers that are divisible by 3 and less than 100, and returns this sum along with the count of such numbers. The function should be able to handle negative numbers in the input list.
"""

def find_divisible_numbers(numbers):
    divisible_numbers = [num for num in numbers if num % 3 == 0 and num < 100]
    sum_of_divisible_numbers = sum(divisible_numbers)
    count_of_divisible_numbers = len(divisible_numbers)
    
    return sum_of_divisible_numbers, count_of_divisible_numbers