"""
QUESTION:
Find the maximum sum of up to four non-adjacent prime numbers in a sorted array. The function should take a sorted array of integers as input and return the maximum sum. Non-adjacent numbers are defined as numbers that do not appear next to each other in the sorted array. The function should return the sum of the maximum number of non-adjacent primes (up to four).
"""

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def max_sum_of_primes(arr):
    primes = [i for i in arr if is_prime(i)]
    if len(primes) <= 4:
        return sum(primes)
    dp = [0]*len(primes)
    dp[0] = primes[0]
    dp[1] = max(primes[0], primes[1])
    dp[2] = primes[0] + primes[2]
    for i in range(3, len(primes)):
        dp[i] = max(primes[i] + dp[i-2], primes[i] + dp[i-3] if i >= 3 else primes[i] + dp[i-2])
        
    return max(dp[-1], dp[-2], dp[-3], dp[-4])