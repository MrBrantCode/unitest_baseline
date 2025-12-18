"""
QUESTION:
Yash likes playing with numbers. He has a challenge for you. Yash gives
you a number that he made by multiplying two numbers. He claims that the
possible sum of the two numbers he multiplied is as minimum as possible. He
challenges you to find that minimum sum.

Formally, for a given value of N, you are required to find the minimum sum of two distinct numbers x and y such that x, y > 0 and xy = N.  

-----Input:-----
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.

Each testcase contains single integer N.

-----Output:-----
For each testcase, output minimum x + y such that x*y = N and x,y >0.

-----Constraints :-----
$1 \leq T \leq 100$
$1 < N \leq 10^{12}$

-----Sample Input:-----
1

852140

-----Sample Output:-----
1929
"""

def find_minimum_sum_of_factors(N):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    if N == 1:
        return 2

    if is_prime(N):
        return N + 1

    if N % 2 == 0:
        k = N // 2
        min_sum = 2 + k
    else:
        min_sum = N + 1

    for j in range(2, N // 2 + 1):
        if N % j == 0:
            k = N // j
            if k != j:
                l = j + k
                if l < min_sum:
                    min_sum = l

    return min_sum