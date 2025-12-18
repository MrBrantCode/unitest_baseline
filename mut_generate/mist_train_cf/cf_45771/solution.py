"""
QUESTION:
Create a function named `product_of_digits` that takes a positive integer `n` as input. The function should calculate the product of the individual digits of `n` that are greater than 2. If no digit is greater than 2, return -1. If `n` is a prime number, append its digits to the result as a composite string.
"""

def product_of_digits(n):
    # Check if n is a prime number
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))
      
    # Calculate the product of the individual digits > 2
    product = 1
    has_digit_greater_than_2 = False
    for digit in str(n):
        if int(digit) > 2:
            product *= int(digit)
            has_digit_greater_than_2 = True
    
    if not has_digit_greater_than_2:
        return -1

    # If n is a prime number, append its digits to the result
    if is_prime(n):
        return str(product) + str(n)
    
    return product