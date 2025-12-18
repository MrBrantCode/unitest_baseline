"""
QUESTION:
Create a function `add_prime_numbers(a, b)` that takes two integers `a` and `b` as input and returns their sum if both are positive prime numbers less than 1000. If either or both numbers are not positive prime integers less than 1000, return an error message specifying the invalid number(s).
"""

def add_prime_numbers(a, b):
    # Check if a and b are positive prime integers less than 1000
    if a < 1 or b < 1 or a >= 1000 or b >= 1000:
        return "Both numbers should be positive prime integers less than 1000"
    
    # Check if a is prime
    is_a_prime = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            is_a_prime = False
            break
    if not is_a_prime:
        return f"{a} is not a prime number"
    
    # Check if b is prime
    is_b_prime = True
    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            is_b_prime = False
            break
    if not is_b_prime:
        return f"{b} is not a prime number"
    
    # Both numbers are prime, so return their sum
    return a + b