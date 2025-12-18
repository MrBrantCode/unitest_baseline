"""
QUESTION:
Create a function `generate_even_numbers` that generates a list of even numbers within a specified range from 1 to n (inclusive) without using any built-in functions. The function should return a list of even integers.
"""

def generate_even_numbers(n):
    even_numbers = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers