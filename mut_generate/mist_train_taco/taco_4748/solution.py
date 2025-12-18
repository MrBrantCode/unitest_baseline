"""
QUESTION:
Given a number $n$, give the last digit of sum of all the prime numbers from 1 to $n$ inclusive.

-----Input:-----
- First line contains number of testcase $t$.
- Each testcase contains of a single line of input, number $n$. 

-----Output:-----
Last digit of sum of every prime number till n.

-----Constraints-----
- $1 \leq T \leq 10$
- $2 \leq N \leq 10^6$

-----Sample Input:-----
1
10

-----Sample Output:-----
7
"""

import math

# Precompute the sum of primes up to 10^6
N = 10 ** 6
sum_arr = [0] * (N + 1)

def precompute_prime_sums():
    arr = [0] * (N + 1)
    arr[0] = 1
    arr[1] = 1
    for i in range(2, math.ceil(math.sqrt(N) + 1)):
        if arr[i] == 0:
            for j in range(i * i, N + 1, i):
                arr[j] = 1
    curr_prime_sum = 0
    for i in range(1, N + 1):
        if arr[i] == 0:
            curr_prime_sum += i
        sum_arr[i] = curr_prime_sum

# Call the precomputation function once
precompute_prime_sums()

def last_digit_of_prime_sum(n):
    """
    Returns the last digit of the sum of all prime numbers from 1 to n.

    Parameters:
    n (int): The upper limit for summing prime numbers.

    Returns:
    int: The last digit of the sum of all prime numbers from 1 to n.
    """
    return sum_arr[n] % 10