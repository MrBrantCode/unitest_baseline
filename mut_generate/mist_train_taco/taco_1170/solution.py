"""
QUESTION:
The binomial coefficient C(N, K) is defined as
N! / K! / (N − K)! for 0 ≤ K ≤ N. 

Here N! = 1 * 2 * ... * N for N ≥ 1, and 0! = 1.

You are given a prime number P and a positive integer N. 

A_{L} is defined as the number of elements in the sequence C(N, K), such that, P^{L} divides C(N, K),
but P^{L+1} does not divide C(N, K). Here, 0 ≤ K ≤ N.

Let M be an integer, such that, A_{M} > 0,
but A_{L} = 0 for all L > M.
Your task is to find numbers A_{0}, A_{1}, ..., A_{M}.

Input Format 

The first line of the input contains an integer T, denoting the number of test cases.
The description of T test cases follows.
The only line of each test case contains two space-separated integers N and P.

Output Format 

For each test case, display M + 1 space separated integers
A_{0}, A_{1}, ..., A_{M}
on the separate line.

Constraints

1 ≤ T ≤ 100 

1 ≤ N ≤ 10^{18} 

2 ≤ P < 10^{18} 

P is prime  

Sample Input

3
4 5
6 3
10 2

Sample Output

5
3 4
4 4 1 2

Explanation  

Example case 1. Values C(4, K) are {1, 4, 6, 4, 1}.
Each of them is not divisible by 5.
Therefore, A_{0} = 5, A_{1} = 0, A_{2} = 0, ..., hence the answer.

Example case 2. Values C(6, K) are {1, 6, 15, 20, 15, 6, 1}.
Among them 1, 20, 1 are not divisible by 3,
while remaining values 6, 15, 15, 6 are divisible by 3, but not divisible by 9.
Therefore, A_{0} = 3, A_{1} = 4,
A_{2} = 0, A_{3} = 0, ..., hence the answer.

Example case 3. Values C(10, K) are {1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1}.
Among them 1, 45, 45, 1 are not divisible by 2,
values 10, 210, 210, 10 are divisible by 2, but not divisible by 4,
value 252 is divisible by 4, but not divisible by 8,
finally, values 120, 120 are divisible by 8, but not divisible by 16.
Therefore, A_{0} = 4, A_{1} = 4,
A_{2} = 1, A_{3} = 2,
A_{4} = 0, A_{5} = 0, ..., hence the answer.
"""

from collections import Counter

def calculate_binomial_coefficients_counts(n, p):
    """
    Calculate the counts A_0, A_1, ..., A_M for the binomial coefficients C(N, K)
    where P^L divides C(N, K) but P^(L+1) does not, for 0 ≤ K ≤ N.

    Parameters:
    n (int): The integer N in the binomial coefficient C(N, K).
    p (int): The prime number P.

    Returns:
    list: A list of integers representing the counts [A_0, A_1, ..., A_M].
    """
    d = []
    nn = n
    while nn != 0:
        d.append(nn % p)
        nn //= p
    
    pprev = Counter()
    nprev = Counter([0])
    
    for di in d:
        ncur = Counter({k: di * v for (k, v) in pprev.items()}) + Counter({k: (di + 1) * v for (k, v) in nprev.items()})
        pcur = Counter({k + 1: (p - di) * v for (k, v) in pprev.items()}) + Counter({k + 1: (p - di - 1) * v for (k, v) in nprev.items()})
        (pprev, nprev) = (pcur, ncur)
    
    return [ncur[i] for i in range(1 + max(ncur.keys()))]