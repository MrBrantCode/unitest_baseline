"""
QUESTION:
Create a function `find_max_prime` that takes three non-negative integer parameters `x`, `y`, and `z`. The function should return the maximum value among `x`, `y`, and `z` if all parameters are prime numbers. If any parameter is negative or not a prime number, the function should return an error message. If all three parameters are zero, the function should return zero. The function should have a time complexity of O(1).
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_prime(x, y, z):
    if x < 0 or y < 0 or z < 0 or not is_prime(x) or not is_prime(y) or not is_prime(z):
        return "Error: Parameters must be non-negative prime numbers"
    
    if x == 0 and y == 0 and z == 0:
        return 0
    
    return max(x, y, z)