"""
QUESTION:
Create a function named `EvenSquaredOddCubedProduct` that takes an integer array as input and returns a tuple. The first element of the tuple should be the sum of squares of the even integers in the array, and the second element should be the product of cubes of the odd integers in the array. If the array contains no even numbers, the first element of the tuple should be 0. If the array contains no odd numbers, the second element of the tuple should be 1.
"""

def EvenSquaredOddCubedProduct(numbers):
    """
    Calculate the sum of squares of even integers and the product of cubes of odd integers in a given array.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the sum of squares of even integers and the product of cubes of odd integers.
    """
    sum_even = 0
    product_odd = 1
    for number in numbers:
        if number % 2 == 0:
            sum_even += number * number
        else:
            product_odd *= number * number * number
    return sum_even, product_odd