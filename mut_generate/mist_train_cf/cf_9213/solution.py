"""
QUESTION:
Create a function called negative_list that takes a list of numbers as input. Return the sum of the negative numbers in the list if the sum is greater than 100; otherwise, return the list of negative numbers. Use list comprehension to find the negative numbers.
"""

def negative_list(numbers):
    negative = [num for num in numbers if num < 0]
    negative_sum = sum(negative)
    return negative_sum if negative_sum > 100 else negative