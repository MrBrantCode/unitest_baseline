"""
QUESTION:
Develop a function `find_all_prime_divisors(n, should_print_all_prime_divisors)` that takes a whole number `n` and a boolean `should_print_all_prime_divisors` as input. The function should return a string indicating whether the number is "prime" or "composite". If the number is composite and `should_print_all_prime_divisors` is True, the function should also return all prime divisors of the composite number. The function should be able to handle inputs up to 10^6 efficiently, with a time complexity better than O(n) and a space complexity better than O(n^2).
"""

import math

def entrance(n, should_print_all_prime_divisors):
    def find_all_prime_divisors(num):
        prime = [True for _ in range(num+1)]
        p = 2
        while(p * p <= num): 
            if (prime[p] == True): 
                for i in range(p * p, num+1, p): 
                    prime[i] = False
            p += 1
        return [p for p in range(2, num) if prime[p] and num % p == 0]

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        sqrt_n = math.isqrt(num) + 1
        for divider in range(3, sqrt_n, 2):
            if num % divider == 0:
                return False
        return True

    if is_prime(n):
        return "Prime"
    else:
        result = "Composite"
        if should_print_all_prime_divisors:
            result += ", Prime divisors: " + str(find_all_prime_divisors(n))
        return result