"""
QUESTION:
Create a function `get_evens_primes_and_merge` that takes two lists of integers `l1` and `l2` as input. The function should return a list containing only the integers that are both even and prime, or just prime, from both input lists. The output list should be sorted in descending order, and all negative integers should be excluded.
"""

def get_evens_primes_and_merge(l1: list, l2: list):
    """Return only even and prime numbers from both lists, merged and sorted in descending order.
    
    Implement a helper function to detect prime numbers.
    """

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

    even_and_prime_numbers = []
    for num1 in l1:
        if num1 % 2 == 0 and num1 > 0:
            even_and_prime_numbers.append(num1)
        elif is_prime(num1) and num1 > 0:
            even_and_prime_numbers.append(num1)

    for num2 in l2:
        if num2 % 2 == 0 and num2 > 0:
            even_and_prime_numbers.append(num2)
        elif is_prime(num2) and num2 > 0:
            even_and_prime_numbers.append(num2)
            
    even_and_prime_numbers.sort(reverse=True)
    return even_and_prime_numbers