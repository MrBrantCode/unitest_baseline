"""
QUESTION:
Write a function `longest_consecutive_primes(s, k)` that finds the longest substring containing only consecutive prime numbers from within the given string `s`. The substring must contain at least `k` prime numbers and be in non-decreasing order of prime numbers. The function takes two parameters: `s`, a string of digits, and `k`, the minimum number of prime numbers required.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def longest_consecutive_primes(s, k):
    max_len = 0
    start_index = -1
    prime_count = 0
    
    for i in range(len(s)):
        if is_prime(int(s[i])):
            prime_count += 1
        else:
            prime_count = 0
            
        if prime_count >= k:
            if i - start_index > max_len:
                max_len = i - start_index + 1
                start_index = i - k + 1
                
    if max_len > 0:
        return s[start_index:start_index + max_len]
    else:
        return ""