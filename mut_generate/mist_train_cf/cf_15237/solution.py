"""
QUESTION:
Create a function called "calculate_sum" that takes a list of integers as a parameter. The function should return the sum of only the even numbers in the input list.
"""

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total