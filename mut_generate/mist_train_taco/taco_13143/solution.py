"""
QUESTION:
You are given an integer N.
Find the number of the positive divisors of N!, modulo 10^9+7.

-----Constraints-----
 - 1≤N≤10^3

-----Input-----
The input is given from Standard Input in the following format:
N

-----Output-----
Print the number of the positive divisors of N!, modulo 10^9+7.

-----Sample Input-----
3

-----Sample Output-----
4

There are four divisors of 3! =6: 1, 2, 3 and 6. Thus, the output should be 4.
"""

import collections

def count_divisors_of_factorial(N: int) -> int:
    mod = 10**9 + 7
    
    # Calculate N!
    factorial = 1
    for i in range(2, N + 1):
        factorial *= i
    
    # Prime factorization of N!
    prime_factors = []
    i = 2
    while i <= factorial:
        if factorial % i == 0:
            prime_factors.append(i)
            factorial //= i
        else:
            i += 1
    
    # Count the occurrences of each prime factor
    count = collections.Counter(prime_factors)
    
    # Calculate the number of divisors
    ans = 1
    for v in count.values():
        ans *= (v + 1)
    
    return ans % mod