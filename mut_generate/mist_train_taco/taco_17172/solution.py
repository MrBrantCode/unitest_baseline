"""
QUESTION:
Dark  with his love for the prime numbers wanted to do some arithmetic so he decided to do some additions.
He wants to generate all prime numbers between two given numbers and add them up and decide whether that addition of numbers is a prime number or not?

Confused, Simply print "YES"(without quotes) if the sum of prime numbers between two numbers is a prime number and print "NO"(without quotes) if the sum of prime numbers between two numbers is a non-prime number.

Note:

If there are no prime numbers between two given numbers print "NO" (without quotes).

Input:

The first line contains T, the number of test cases.
Followed by T lines each contain two numbers M and N

Output:

For every test case print the YES if sum is a prime number else print NO.

If no prime number between M and N
then print NO.

Constraints

   1 ≤ T ≤ 10000
   1 ≤ M ≤ N ≤ 1000000

Note: 'M' & 'N'  are inclusive.

Author : Darshak Mehta

SAMPLE INPUT
3
1 9
14 37
1 6

SAMPLE OUTPUT
YES
NO
NO

Explanation

Test Case #1:
Prime numbers between 1 to 9 are 2,3,5,7 and their sum is 17 which is a prime number.

Test Case #3:
Prime numbers between 1 to 6 are 2,3,5 and their sum is 10 which is non-prime number
"""

def check_prime_sums(T, test_cases):
    import bisect, math

    def primes_upto(limit):
        is_prime = [False] * 2 + [True] * (limit - 1) 
        for n in range(int(limit**0.5 + 1.5)):
            if is_prime[n]:
                for i in range(n*n, limit+1, n):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]

    def iprimes2(limit):
        yield 2
        if limit < 3: return
        lmtbf = (limit - 3) // 2
        buf = [True] * (lmtbf + 1)
        for i in range((int(limit ** 0.5) - 3) // 2 + 1):
            if buf[i]:
                p = i + i + 3
                s = p * (i + 1) + i
                buf[s::p] = [False] * ((lmtbf - s) // p + 1)
        for i in range(lmtbf + 1):
            if buf[i]: yield (i + i + 3)

    def is_prime(n):
        if n == 2:
            return "YES"
        if n % 2 == 0 or n <= 1:
            return "NO"
        sqr = int(math.sqrt(n)) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return "NO"
        return "YES"

    l = list(iprimes2(1000001))
    length = len(l)
    results = []

    for m, n in test_cases:
        idx = bisect.bisect_left(l, m)
        s = 0
        while idx < length and l[idx] <= n:
            s += l[idx]
            idx += 1
        results.append(is_prime(s))

    return results