"""
QUESTION:
Implement a function `sum` that takes a list of numbers and returns their total sum without using mutable variables or shared state. The function should be designed with functional programming principles in mind, ensuring immutability and avoiding side effects.
"""

def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total