"""
QUESTION:
Write a function called `find_max_substring` that finds the maximum substring with a specific length `k` in a given string `s`, where `k` is a prime number. The function should return the maximum substring with length `k` from `s`. The input is a string `s` and an integer `k`, and the output is the maximum substring with length `k` from `s`.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_max_substring(s, k):
    max_substring = ""
    for i in range(len(s) - k + 1):
        if is_prime(k):
            substring = s[i:i+k]
            if len(substring) > len(max_substring):
                max_substring = substring
    return max_substring