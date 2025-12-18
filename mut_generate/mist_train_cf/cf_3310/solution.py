"""
QUESTION:
Implement a function named `append_primes` that takes two lists of integers, `listA` and `listB`, as input. The function should append the prime numbers from `listB` to `listA`, remove duplicates, sort the resulting list in ascending order, and ensure it does not exceed 1000 elements. The prime numbers in `listB` must be sorted in descending order before being appended to `listA`. The function should not use any built-in sorting functions or data structures.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def append_primes(listA, listB):
    primes = []
    for num in listB:
        if is_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    for num in primes:
        listA.append(num)
    listA = list(set(listA))
    listA.sort()
    if len(listA) > 1000:
        listA = listA[:1000]
    return listA