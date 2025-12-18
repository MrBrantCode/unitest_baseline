"""
QUESTION:
Write a function named `longest_consecutive_primes` that takes two parameters: a string `s` containing digits and an integer `k`. The function should return the longest substring from `s` that contains at least `k` consecutive prime numbers in non-decreasing order. If there are multiple substrings with the same maximum length, any of them can be returned.
"""

def longest_consecutive_primes(s, k):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

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
                max_len = i - start_index
                start_index = i - k + 1
                
    longest_substring = s[start_index:start_index + max_len]
    return longest_substring