"""
QUESTION:
Find the maximum product of 13 consecutive digits in a given 1000-digit number. 

The function should take a string of 1000 digits as input and return the numerical value of the maximum product. 

The input string will only contain digits and may contain newline characters that should be ignored. 

The function should return the maximum product of any 13 consecutive digits in the input string.
"""

def max_consecutive_product(num_str, n):
    """
    This function calculates the maximum product of 'n' consecutive digits in a given string of digits.
    
    Parameters:
    num_str (str): The input string of digits.
    n (int): The number of consecutive digits to consider for the product.
    
    Returns:
    int: The maximum product of 'n' consecutive digits.
    """
    max_product = 0
    num_str = num_str.replace('\n', '')
    
    for i in range(0, len(num_str) - n + 1):
        product = 1
        for j in num_str[i: i + n]:
            product *= int(j)
        if product > max_product:
            max_product = product
    
    return max_product

# To find the maximum product of 13 consecutive digits, call the function with n = 13
# max_product = max_consecutive_product(number, 13)