"""
QUESTION:
Write a function called `generate_even_numbers` that generates the first 'n' even numbers in reverse order. The function should take one parameter 'n', which represents the number of even numbers to generate. For example, when 'n' is 10, the output should be a list of the first 10 even numbers in descending order.
"""

def generate_even_numbers(n):
    return [i for i in range(n*2, 0, -2)]