"""
QUESTION:
Write a function called `swapPrimes` that takes two lists of integers `lst1` and `lst2` as input, and returns a string indicating whether a specific condition is met. The function should use a Sieve of Eratosthenes to identify prime numbers up to 10^6. It should attempt to swap a non-prime element in `lst1` with a prime element in `lst2`, and check if the sums of both lists remain unchanged after the swap. If no swap is possible, the function should check if all elements in `lst1` are prime. The function should return "YES" if the condition is met and "NO" otherwise.
"""

def swapPrimes(lst1, lst2):
    sieve = [True for _ in range(10**6+1)]
    sieve[0] = sieve[1] = False
    p = 2
    while(p * p <= 10**6):
        if (sieve[p] == True):
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