"""
QUESTION:
A number is called almost prime if it has exactly two distinct prime divisors. For example, numbers 6, 18, 24 are almost prime, while 4, 8, 9, 42 are not. Find the amount of almost prime numbers which are between 1 and n, inclusive.

Input

Input contains one integer number n (1 ≤ n ≤ 3000).

Output

Output the amount of almost prime numbers between 1 and n, inclusive.

Examples

Input

10


Output

2


Input

21


Output

8
"""

from math import sqrt

def count_almost_prime_numbers(n):
    # Step 1: Generate a list of prime numbers up to 3000
    numbers = list(range(3000))
    primes = []
    
    for i in numbers:
        if i != 0 and i != 1:
            non_prime_value = i + i
            while non_prime_value < len(numbers):
                numbers[non_prime_value] = 0
                non_prime_value += i
    
    for i in numbers:
        if i != 0 and i != 1:
            primes.append(i)
    
    # Step 2: Count almost prime numbers between 1 and n
    count = 0
    for i in range(4, n + 1):
        local_count = 0
        value = i
        prime_index = 0
        while prime_index < len(primes) and primes[prime_index] <= value:
            if value % primes[prime_index] == 0:
                local_count += 1
                while value % primes[prime_index] == 0:
                    value = value // primes[prime_index]
            prime_index += 1
            if local_count == 2 and value == 1:
                count += 1
                break
    
    return count