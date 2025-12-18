"""
QUESTION:
Create a function named `prime_product_dict` that takes two parameters, `x` and `y`, where `x` is a prime number greater than 10,000 and `y` is a prime number greater than 1,000. This function should return a dictionary where each key is a unique prime number between `x` and `y` (inclusive), and the value of each key is the product of `x` and `y`.
"""

def prime_product_dict(x, y):
    prime_product = {}
    
    for i in range(x, y+1):
        is_prime = True
        
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_product[i] = x * y
    
    return prime_product