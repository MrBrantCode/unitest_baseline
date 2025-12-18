"""
QUESTION:
Create a function `find_even_numbers` that takes a list of numbers as input. The function should return a tuple containing a list of even integers in descending order and the sum of these even integers. The function should also handle non-numeric inputs and raise an error if the input list contains non-numeric values.
"""

def find_even_numbers(input_list):
    even_numbers = [i for i in input_list if isinstance(i, int) and i%2 == 0]
    even_numbers.sort(reverse=True)
    aggregate = sum(even_numbers)
    return (even_numbers, aggregate)