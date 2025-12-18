"""
QUESTION:
Create a function named `find_max_prime(x, y, z)` that takes three non-negative integer parameters and returns the maximum value among them. The function should only accept prime numbers as input. If any of the parameters are negative or not prime, the function should return an error message. If all three parameters are zero, the function should return zero.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_prime(x, y, z):
    # Check if any of the parameters are negative or not prime
    if x < 0 or y < 0 or z < 0 or not is_prime(x) or not is_prime(y) or not is_prime(z):
        return "Error: Parameters must be non-negative prime numbers"
    
    # Check if all parameters are zero
    if x == 0 and y == 0 and z == 0:
        return 0
    
    # Return the maximum value
    return max(x, y, z)