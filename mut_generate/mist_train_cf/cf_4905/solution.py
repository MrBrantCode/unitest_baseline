"""
QUESTION:
Implement a function named `print_prime_with_prime_digit_sum` that takes an array of integers as input. This function should iterate over each number in the array, check if the number is prime, and calculate the sum of its digits. If the number is prime and the sum of its digits is also prime, print the number followed by its prime factors. The prime factors should be printed in ascending order and separated by commas. If the number has no prime factors (i.e., it is a prime number itself), print "None".
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def print_prime_with_prime_digit_sum(nums):
    for num in nums:
        if is_prime(num):
            digit_sum = sum([int(digit) for digit in str(num)])
            if is_prime(digit_sum):
                prime_factors = get_prime_factors(num)
                if prime_factors:
                    prime_factors_str = ', '.join(map(str, prime_factors))
                    print(f"{num}: Prime factors: {prime_factors_str}")
                else:
                    print(f"{num}: Prime factors: None")