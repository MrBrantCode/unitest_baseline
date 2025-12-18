"""
QUESTION:
Write a function named `sum_of_products_of_digits` that calculates the sum of the products of the digits of a given number with its reverse. The function should take an integer as input and return the calculated sum.
"""

def sum_of_products_of_digits(n):
    """
    Calculate the sum of the products of the digits of a given number with its reverse.

    Args:
        n (int): The input number.

    Returns:
        int: The sum of the products of the digits of the number with its reverse.
    """
    # Convert the number to a string to easily access each digit
    str_n = str(n)
    
    # Reverse the string
    reversed_str_n = str_n[::-1]
    
    # Initialize the sum of products
    total_sum = 0
    
    # Iterate over the digits in the string
    for i in range(len(str_n)):
        # Multiply the current digit with its corresponding digit in the reversed string
        # and add the result to the total sum
        total_sum += int(str_n[i]) * int(reversed_str_n[i])
    
    return total_sum