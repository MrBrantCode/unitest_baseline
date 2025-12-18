"""
QUESTION:
Create a function `add_prime_numbers(a, b)` that takes two integers `a` and `b` as arguments and returns their sum. The function should only accept positive prime integers less than 1000 as valid inputs. If either `a` or `b` is not a positive prime integer less than 1000, the function should return an error message.
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