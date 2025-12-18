"""
QUESTION:
Construct a function `check_product_is_prime` that takes a list of whole numbers as input and returns a Boolean value indicating whether the product of these numbers is a prime number. The function should consider 1 and all even numbers (except 2) as non-prime.
"""

def check_product_is_prime(numbers):
    def check_if_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    product = 1
    for num in numbers:
        product *= num
    return check_if_prime(product)