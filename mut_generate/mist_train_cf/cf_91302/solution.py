"""
QUESTION:
Create a function named `prime_product_dict` that takes two parameters: `x` and `y`, both of which are prime numbers. The function should return a dictionary where each key is a unique prime number in the range from `x` to `y` (inclusive) and the value of each key is the product of `x` and `y`. Assume that `x` is greater than 10,000 and `y` is greater than 1,000.
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