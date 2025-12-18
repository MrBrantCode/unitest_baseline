"""
QUESTION:
Write a function named `binary_prime_test` that takes a two-digit binary number as a string input and returns a tuple containing the decimal equivalent, binary representation, primality, prime factors (if not prime), and palindrome status of the input number. The function should use the trial division method for primality testing and should only handle binary inputs.
"""

def binary_prime_test(binary):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    def prime_factors(n):
        factors = []
        for i in range(2, n+1):
            while n % i == 0:
                factors.append(i)
                n //= i
            if n == 1:
                break
        return factors
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    def binary_to_decimal(binary):
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        return decimal

    decimal = binary_to_decimal(binary)
    prime = is_prime(decimal)
    factors = prime_factors(decimal) if not prime else []
    palindrome = is_palindrome(decimal)
    return decimal, binary, prime, factors, palindrome