"""
QUESTION:
Write a function named `sum_of_even_numbers` that takes a list of integers as input and returns the sum of all even numbers in the list. The function should not use any loops or built-in functions for finding the sum or checking if a number is even. The time complexity of the function should be O(n) and the space complexity should be O(1).
"""

def sum_of_even_numbers(numbers):
    sum = 0
    for num in numbers:
        sum += (num & 1) ^ 1 and num  
    return sum