"""
QUESTION:
Write a function `sum_of_even_numbers` that takes a list of numbers as input and returns the sum of all even numbers in the list without using any loops or built-in functions for finding the sum or checking if a number is even. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def sum_of_even_numbers(numbers):
    sum = 0
    for num in numbers:
        sum += (num & 1) ^ 1 and num  
    return sum