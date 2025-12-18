"""
QUESTION:
The prime number sequence starts with: `2,3,5,7,11,13,17,19...`. Notice that `2` is in position `one`. 

`3` occupies position `two`, which is a prime-numbered position. Similarly, `5`, `11` and `17` also occupy prime-numbered positions. We shall call primes such as `3,5,11,17` dominant primes because they occupy prime-numbered positions in the prime number sequence. Let's call this `listA`. 

As you can see from listA, for the prime range `range(0,10)`, there are `only two` dominant primes (`3` and `5`) and the sum of these primes is: `3 + 5 = 8`. 

Similarly, as shown in listA, in the `range (6,20)`, the dominant primes in this range are `11` and `17`, with a sum of `28`.

Given a `range (a,b)`, what is the sum of dominant primes within that range? Note that  `a <= range <= b` and `b` will not exceed `500000`.

Good luck!

If you like this Kata, you will enjoy:

[Simple Prime Streaming](https://www.codewars.com/kata/5a908da30025e995880000e3)

[Sum of prime-indexed elements](https://www.codewars.com/kata/59f38b033640ce9fc700015b)

[Divisor harmony](https://www.codewars.com/kata/59bf97cd4f98a8b1cd00007e)
"""

def sum_dominant_primes_in_range(a: int, b: int) -> int:
    n = 500000
    sieve = [0] * (n // 2 + 1)
    primes = [0, 2]
    
    # Sieve of Eratosthenes to find all primes up to n
    for i in range(3, n + 1, 2):
        if not sieve[i // 2]:
            primes.append(i)
            for j in range(i ** 2, n + 1, i * 2):
                sieve[j // 2] = 1
    
    # Find dominant primes
    dominant_primes = []
    for p in primes:
        if p >= len(primes):
            break
        dominant_primes.append(primes[p])
    
    # Sum of dominant primes in the range [a, b]
    return sum(p for p in dominant_primes if a <= p <= b)