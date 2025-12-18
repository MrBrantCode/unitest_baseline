"""
QUESTION:
Create a function called `powers_of_two_and_three` that takes an integer `n` as input. Calculate the sum of all powers of 2 up to 2^n and the product of all powers of 3 up to 3^n, then return or print these two values. The function should not take any other inputs.
"""

def powers_of_two_and_three(n):
    """
    Calculate the sum of all powers of 2 up to 2^n and 
    the product of all powers of 3 up to 3^n.

    Args:
        n (int): The input number.

    Returns:
        tuple: A tuple containing the sum of powers of 2 and the product of powers of 3.
    """
    # Calculate the sum of powers of 2 up to 2^n
    sum_of_powers_of_2 = sum(2 ** i for i in range(n + 1))

    # Calculate the product of powers of 3 up to 3^n
    product_of_powers_of_3 = 1
    for i in range(n + 1):
        product_of_powers_of_3 *= 3 ** i

    return sum_of_powers_of_2, product_of_powers_of_3