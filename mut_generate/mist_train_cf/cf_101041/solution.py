"""
QUESTION:
Write a function `is_prime` to generate the first 10 prime numbers between 1000 and 2000. The function should calculate the sum of their digits, display the prime numbers in a table format, and convert the sum of the digits to binary before displaying the result.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def entance():
    primes = []
    for n in range(1000, 2000):
        if is_prime(n):
            primes.append(n)
            if len(primes) == 10:
                break
    sum_of_digits = sum(int(digit) for prime in primes for digit in str(prime))
    binary_sum = bin(sum_of_digits)[2:]
    print("First 10 prime numbers between 1000 and 2000:")
    print("+" + "-"*8 + "+")
    print("| {:^6} |".format("Prime"))
    print("+" + "-"*8 + "+")
    for prime in primes:
        print("| {:^6} |".format(prime))
    print("+" + "-"*8 + "+")
    print("Sum of digits of the primes: {}".format(sum_of_digits))
    print("Binary representation of the sum of digits: {}".format(binary_sum))