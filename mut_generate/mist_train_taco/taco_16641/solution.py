"""
QUESTION:
Chef likes prime numbers. However, there is one thing he loves even more. Of course, it's semi-primes! A semi-prime number is an integer which can be expressed as a product of two distinct primes. For example, $15 = 3 \cdot 5$ is a semi-prime number, but $1$, $9 = 3 \cdot 3$ and $5$ are not.
Chef is wondering how to check if an integer can be expressed as a sum of two (not necessarily distinct) semi-primes. Help Chef with this tough task!

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

-----Output-----
For each test case, print a single line containing the string "YES" if it is possible to express $N$ as a sum of two semi-primes or "NO" otherwise.

-----Constraints-----
- $1 \le T \le 200$
- $1 \le N \le 200$

-----Example Input-----
3
30
45
62

-----Example Output-----
YES
YES
NO

-----Explanation-----
Example case 1: $N=30$ can be expressed as $15 + 15 = (3 \cdot 5) + (3 \cdot 5)$.
Example case 2: $45$ can be expressed as $35 + 10 = (5 \cdot 7) + (2 \cdot 5)$.
Example case 3: $62$ cannot be expressed as a sum of two semi-primes.
"""

def can_be_sum_of_two_semi_primes(N):
    n = 201
    v = [0 for i in range(n + 1)]

    def gen():
        for i in range(1, n + 1):
            v[i] = i
        countDivision = [0 for i in range(n + 1)]
        for i in range(n + 1):
            countDivision[i] = 2
        for i in range(2, n + 1, 1):
            if v[i] == i and countDivision[i] == 2:
                for j in range(2 * i, n + 1, i):
                    if countDivision[j] > 0:
                        v[j] = int(v[j] / i)
                        countDivision[j] -= 1

    gen()
    flag = 0
    for i in range(2, N // 2 + 1):
        if v[i] == 1 and v[N - i] == 1:
            flag = 1
            break
    
    return "YES" if flag == 1 else "NO"