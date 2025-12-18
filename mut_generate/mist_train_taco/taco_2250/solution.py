"""
QUESTION:
Pak Chanek has a prime number$^\dagger$ $n$. Find a prime number $m$ such that $n + m$ is not prime.

$^\dagger$ A prime number is a number with exactly $2$ factors. The first few prime numbers are $2,3,5,7,11,13,\ldots$. In particular, $1$ is not a prime number.


-----Input-----

Each test contains multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 10^4$) — the number of test cases. The following lines contain the description of each test case.

The only line of each test case contains a prime number $n$ ($2 \leq n \leq 10^5$).


-----Output-----

For each test case, output a line containing a prime number $m$ ($2 \leq m \leq 10^5$) such that $n + m$ is not prime. It can be proven that under the constraints of the problem, such $m$ always exists.

If there are multiple solutions, you can output any of them.


-----Examples-----

Input
3
7
2
75619
Output
2
7
47837


-----Note-----

In the first test case, $m = 2$, which is prime, and $n + m = 7 + 2 = 9$, which is not prime.

In the second test case, $m = 7$, which is prime, and $n + m = 2 + 7 = 9$, which is not prime.

In the third test case, $m = 47837$, which is prime, and $n + m = 75619 + 47837 = 123456$, which is not prime.
"""

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_non_prime_sum_prime(n):
    m = 2
    while True:
        if is_prime(m) and not is_prime(n + m):
            return m
        m += 1