"""
QUESTION:
Implement a function `append_primes(listA, listB)` that takes two lists of integers as input, appends prime numbers from `listB` to `listA`, removes duplicates, and sorts the resulting list in ascending order. The prime numbers from `listB` should be sorted in descending order before appending to `listA`. The resulting list should not exceed 1000 elements. The algorithm should have a time complexity of O(n log n) and should not use any built-in sorting functions or data structures.
"""

def append_primes(listA, listB):
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