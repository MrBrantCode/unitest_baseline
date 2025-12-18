"""
QUESTION:
Given two non-empty lists of integers, write a function `switch` that takes these lists as input and determines whether it's possible to exchange elements between them such that the first list contains only prime numbers and the cumulative sum of both lists remains the same. The function should return "YES" if this is possible and "NO" otherwise.
"""

def switch(lst1, lst2):
    # Function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # Filter the prime and non-prime numbers in both lists
    primes_in_lst1 = list(filter(is_prime, lst1))
    non_primes_in_lst1 = list(filter(lambda x: not is_prime(x), lst1))
    primes_in_lst2 = list(filter(is_prime, lst2))
    non_primes_in_lst2 = list(filter(lambda x: not is_prime(x), lst2))

    # Check if sum of all prime and non-prime numbers remains constant after the switch
    if sum(primes_in_lst1) + sum(non_primes_in_lst2) != sum(non_primes_in_lst1) + sum(primes_in_lst2):
        return "NO"
    
    return "YES"