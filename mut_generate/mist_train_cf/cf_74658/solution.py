"""
QUESTION:
Implement a function named `validate_number` that takes one integer `n` as input. The function should return a string indicating whether the number is a prime number and its parity (even or odd) if it is prime, or a message stating that the number is not prime. The function should not use any built-in prime-checking functions or libraries. A prime number is a natural number greater than 1 with no positive divisors other than 1 and itself.
"""

def validate_number(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return str(n) + " is not a prime number"
                break
        else:
            return str(n) + " is a prime number and it's " + ("even" if n % 2 == 0 else "odd")
    else:
        return str(n) + " is not a prime number"