"""
QUESTION:
Define a function `swapPrimes(lst1, lst2)` that takes two non-empty lists of integers as input and returns "YES" if a valid permutation can be created by swapping single or multiple elements between the lists to transform `lst1` into a list of prime numbers while keeping the sum of all array elements constant, and "NO" otherwise. The function should use the sieve of Eratosthenes for prime number identification and handle integers up to 10^6.
"""

def swap_primes(lst1, lst2):
    sieve = [True for _ in range(10**6+1)]
    sieve[0] = False
    sieve[1] = False
    p = 2
    while p * p <= 10**6:
        if sieve[p]:
            for i in range(p * p, 10**6+1, p):
                sieve[i] = False
        p += 1

    sum1 = sum(lst1)
    sum2 = sum(lst2)
    change = False

    for i in range(len(lst1)):
        if not sieve[lst1[i]]:
            for j in range(len(lst2)):
                if sieve[lst2[j]]:
                    temp = lst1[i]
                    lst1[i] = lst2[j]
                    lst2[j] = temp
                    change = True
                    break
            if change:
                break

    if change:
        return "YES" if sum(lst1) == sum1 and sum(lst2) == sum2 else "NO"
    else:
        if all(sieve[i] for i in lst1):
            return "YES"
        else:
            return "NO"