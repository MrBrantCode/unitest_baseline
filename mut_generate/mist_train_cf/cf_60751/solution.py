"""
QUESTION:
Create a function named `kth_smallest_prime` that takes two parameters: a list of integers `arr` and an integer `k`. The function should find the kth smallest prime number in the given array. If the array has fewer than k prime numbers, it should return a message indicating this. The prime numbers should be identified by checking divisibility up to the number itself, and the list of prime numbers should be sorted before selecting the kth smallest prime. The function should return the kth smallest prime number if it exists.
"""

def kth_smallest_prime(arr, k):
    primes = []
    for num in arr:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    primes.sort()
    if len(primes) >= k:
        return primes[k-1]
    else:
        return "Not enough primes in the array"