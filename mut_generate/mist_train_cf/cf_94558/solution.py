"""
QUESTION:
Implement a function called `find_even_numbers` that takes a list of integers as input and returns a list of even numbers from the input list.
"""

def find_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers