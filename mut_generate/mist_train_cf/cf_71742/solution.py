"""
QUESTION:
Create a function named `rearrange_numbers` that takes an array of integers as input and rearranges its elements such that all even numbers (excluding the prime number 2) come before all odd numbers. The prime number 2 should be placed at the beginning of all even numbers, and odd prime numbers should be placed at the end of all odd numbers. The input array will contain numbers ranging from 1 to 10,000. The solution should prioritize low time and space complexity.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def rearrange_numbers(arr):
    even_primes = [x for x in arr if x == 2]
    other_evens = [x for x in arr if x % 2 == 0 and x != 2]
    odd_primes = [x for x in arr if x % 2 != 0 and is_prime(x)]
    other_odds = [x for x in arr if x % 2 != 0 and not is_prime(x)]

    return even_primes + other_evens + other_odds + odd_primes