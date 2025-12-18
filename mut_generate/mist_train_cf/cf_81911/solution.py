"""
QUESTION:
Create a function called `find_even_product_pair` that takes a list of integers as input and returns `True` if the multiplication of any two distinct integers in the list yields an even number, and `False` otherwise. The function should be optimized to handle large sets of data effectively. It should also handle edge cases such as an empty list, a list with one element, and lists that consist only of odd numbers.
"""

def find_even_product_pair(numbers):
    if not numbers or len(numbers) < 2:
        return False

    for i in numbers:
        if i % 2 == 0:
            return True

    return False