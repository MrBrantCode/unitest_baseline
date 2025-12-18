"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given number using a while loop. The function should only perform the factorial calculation if the input number is prime, and it should return a message indicating this restriction if the input number is not prime.
"""

def factorial(n):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(n):
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
    else:
        return "Factorial calculation is only performed for prime numbers."