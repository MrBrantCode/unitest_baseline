"""
QUESTION:
Create a function `is_prime` that takes an integer `num` and an optional parameter `divisor` (default value 2) and returns a boolean indicating whether `num` is a prime number. The function must only use recursion to determine if `num` is prime and should not use loops or built-in prime-checking functions. Additionally, if `num` is not a positive integer, the function should prompt the user to enter a valid positive integer and recursively call itself with the new input.
"""

def is_prime(num, divisor=2):
    # Check for non-integer or negative input
    if not isinstance(num, int) or num < 1:
        num = int(input("Enter a positive integer: "))
        return is_prime(num, 2)
    
    # Base cases
    if num == 1:
        return False
    if num == 2:
        return True
    
    # Recursive case
    if num % divisor == 0:
        return False
    if divisor * divisor > num:
        return True
    
    return is_prime(num, divisor + 1)