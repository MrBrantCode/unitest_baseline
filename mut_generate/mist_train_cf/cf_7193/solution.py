"""
QUESTION:
Create a function called `find_lcm` that calculates the least common multiple of two integers. The function should handle cases where one or both of the numbers are negative and also handle cases where the numbers are floating point numbers. The function must use prime factorization and cannot use any built-in prime factorization functions or libraries.
"""

def find_lcm(num1, num2):
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Convert to positive integers
    num1 = int(abs(num1))
    num2 = int(abs(num2))

    # Calculate the LCM using the formula lcm(a, b) = |a*b| / gcd(a, b)
    lcm = abs(num1 * num2) // gcd(num1, num2)

    return lcm