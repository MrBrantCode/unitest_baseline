"""
QUESTION:
Marin wants you to count number of permutations that are beautiful. A beautiful permutation of length $n$ is a permutation that has the following property: $$ \gcd (1 \cdot p_1, \, 2 \cdot p_2, \, \dots, \, n \cdot p_n) > 1, $$ where $\gcd$ is the greatest common divisor .

A permutation is an array consisting of $n$ distinct integers from $1$ to $n$ in arbitrary order. For example, $[2,3,1,5,4]$ is a permutation, but $[1,2,2]$ is not a permutation ($2$ appears twice in the array) and $[1,3, 4]$ is also not a permutation ($n=3$ but there is $4$ in the array).


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10^3$) — the number of test cases.

Each test case consists of one line containing one integer $n$ ($1 \le n \le 10^3$).


-----Output-----

For each test case, print one integer — number of beautiful permutations. Because the answer can be very big, please print the answer modulo $998\,244\,353$.


-----Examples-----

Input
7
1
2
3
4
5
6
1000
Output
0
1
0
4
0
36
665702330


-----Note-----

In first test case, we only have one permutation which is $[1]$ but it is not beautiful because $\gcd(1 \cdot 1) = 1$.

In second test case, we only have one beautiful permutation which is $[2, 1]$ because $\gcd(1 \cdot 2, 2 \cdot 1) = 2$.
"""

def count_beautiful_permutations(t: int, test_cases: list[int]) -> list[int]:
    """
    Counts the number of beautiful permutations for each test case.

    A beautiful permutation of length `n` is a permutation where the greatest common divisor (gcd) of 
    the products of the indices and their corresponding values is greater than 1.

    Args:
        t (int): The number of test cases.
        test_cases (list[int]): A list of integers where each integer represents the length `n` of a permutation.

    Returns:
        list[int]: A list of integers where each integer represents the number of beautiful permutations 
                   for the corresponding test case, modulo 998244353.
    """
    mod = 998244353
    f = [1]
    for i in range(1, 1001):
        f.append(f[i - 1] * i % mod)
    
    results = []
    for n in test_cases:
        if n % 2 == 1:
            results.append(0)
        else:
            results.append(f[n // 2] * f[n // 2] % mod)
    
    return results