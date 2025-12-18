"""
QUESTION:
Create a function named `check_product` that takes an array of integers and/or floating point numbers as input. The function should determine whether the cumulative multiplication of the array elements is even or odd and find the position of the first odd integer in the array. If no odd integers are found, the function should return -1 as the position. The function should round floating point numbers to the nearest integer before processing them and terminate as soon as it encounters a zero (returning 'even' and -1) or an even cumulative product.
"""

def check_product(numbers):
    # Initialize the product and set the first odd index to -1
    product = 1
    first_odd_index = -1

    for i in range(len(numbers)):
        # Check if the number is a float and round it
        if isinstance(numbers[i], float):
            numbers[i] = round(numbers[i])

        # If the number is zero, return ('even', -1) immediately since the product is even
        if numbers[i] == 0:
            return 'even', -1

        # If the number is odd and first_odd_index hasn't been updated yet, update it
        if numbers[i] % 2 != 0 and first_odd_index == -1:
            first_odd_index = i

        # Multiply the current number with the product
        product *= numbers[i]

        # As soon as you find that the product has become even, return ('even', first_odd_index)
        if product % 2 == 0:
            return 'even', first_odd_index

    # If the product is odd return ('odd', first_odd_index)
    return 'odd', first_odd_index