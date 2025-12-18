"""
QUESTION:
Write a function `sum_even_product_odd` that takes an integer `number` as input, calculates the sum of all even numbers between 0 and the given `number`, and returns the sum along with the product of all odd numbers in the same range.
"""

def sum_even_product_odd(number):
    """
    This function calculates the sum of all even numbers between 0 and the given number, 
    and returns the sum along with the product of all odd numbers in the same range.

    Args:
        number (int): The input number up to which the calculation is performed.

    Returns:
        tuple: A tuple containing the sum of even numbers and the product of odd numbers.
    """
    sum_even = 0
    product_odd = 1

    for i in range(1, number+1):
        if i % 2 == 0:
            sum_even += i
        else:
            product_odd *= i
    
    return sum_even, product_odd