"""
QUESTION:
Calculate the last 10 digits of the product of 50 given 100-digit numbers. 

Function name: None. 

Information: The input is a list of 50 100-digit numbers. The output is the last 10 digits of their product. 

Restriction: The solution should use modular arithmetic to efficiently calculate the result.
"""

def last_ten_digits_product(nums):
    """
    Calculate the last 10 digits of the product of a list of numbers.

    Args:
    nums (list): A list of numbers as strings.

    Returns:
    int: The last 10 digits of the product of the input numbers.
    """
    modulus = 10**10
    product = 1

    for num in nums:
        product = (product * int(num)) % modulus

    return product