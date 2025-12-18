"""
QUESTION:
Write a function named sum_even_numbers that takes two parameters: max_number and step_size. The function should calculate and return the sum of all even numbers between 0 and max_number (inclusive), with the range of numbers incremented by the step_size.
"""

def sum_even_numbers(max_number, step_size):
    sum = 0
    for i in range(0, max_number + 1, step_size):
        if i % 2 == 0:
            sum += i
    return sum